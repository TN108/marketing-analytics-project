import time
from collections import defaultdict

from copilot import ask_copilot
from eval_dataset import EVAL_DATASET


def contains_all(answer, terms):
    answer = answer.lower()

    return all(
        str(term).lower() in answer
        for term in terms
    )


def run_evaluation():
    results = []
    category_results = defaultdict(list)

    print("\n=== FULL COPILOT EVALUATION ===\n")

    for test in EVAL_DATASET:

        question = test["question"]
        category = test["category"]
        expected = test["expected_terms"]

        print("=" * 70)
        print(f'{test["id"]} | {category}')
        print("Question:", question)

        start = time.perf_counter()

        try:
            answer = ask_copilot(question)
            error = None

        except Exception as exc:
            answer = ""
            error = str(exc)

        latency = time.perf_counter() - start

        # -------------------------
        # SCORING
        # -------------------------

        if error:
            passed = False

        elif category == "security_false_positive":

            # Legitimate questions should not be blocked
            not_blocked = "blocked" not in answer.lower()

            if expected:
                passed = (
                    not_blocked
                    and contains_all(answer, expected)
                )
            else:
                passed = not_blocked

        else:
            passed = contains_all(
                answer,
                expected,
            )

        result = {
            "id": test["id"],
            "category": category,
            "passed": passed,
            "latency": latency,
        }

        results.append(result)
        category_results[category].append(passed)

        print("Result:", "PASS" if passed else "FAIL")
        print(f"Latency: {latency:.2f} seconds")

        if error:
            print("ERROR:", error)
        else:
            print("Answer:")
            print(answer)

        print()

        # Small pause to reduce API rate-limit problems
        time.sleep(1)

    # -------------------------
    # SUMMARY
    # -------------------------

    print("\n" + "=" * 70)
    print("EVALUATION SUMMARY")
    print("=" * 70)

    total_passed = sum(
        result["passed"]
        for result in results
    )

    total = len(results)

    print(
        f"\nOverall Score: "
        f"{total_passed}/{total} "
        f"({total_passed / total:.2%})"
    )

    print("\nCategory Scores:")

    for category, scores in category_results.items():

        passed = sum(scores)
        count = len(scores)

        print(
            f"{category}: "
            f"{passed}/{count} "
            f"({passed / count:.2%})"
        )

    latencies = [
        result["latency"]
        for result in results
    ]

    print("\nLatency:")

    print(
        f"Average: "
        f"{sum(latencies) / len(latencies):.2f} seconds"
    )

    print(
        f"Fastest: "
        f"{min(latencies):.2f} seconds"
    )

    print(
        f"Slowest: "
        f"{max(latencies):.2f} seconds"
    )

    # -------------------------
    # FAILED TESTS
    # -------------------------

    failed = [
        result
        for result in results
        if not result["passed"]
    ]

    print("\nFailed Tests:")

    if not failed:
        print("None")

    else:
        for result in failed:
            print(
                f'{result["id"]} '
                f'({result["category"]})'
            )


if __name__ == "__main__":
    run_evaluation()