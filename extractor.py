import argparse
import json
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Extract one column (list) from a Trello board JSON export."
    )
    parser.add_argument("board_file", help="path to the Trello board JSON export")
    parser.add_argument("column_name", help="exact (case-sensitive) list name")
    args = parser.parse_args()

    try:
        with open(args.board_file, encoding="utf-8") as f:
            board = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        sys.exit(f"cannot read board file: {e}")

    lists = board.get("lists", [])
    target = next((lst for lst in lists if lst.get("name") == args.column_name), None)
    if target is None:
        names = ", ".join(repr(lst.get("name")) for lst in lists)
        sys.exit(f"column not found: {args.column_name}\navailable lists: {names}")

    cards = [
        card
        for card in board.get("cards", [])
        if card.get("idList") == target["id"] and not card.get("closed")
    ]
    cards.sort(key=lambda card: card.get("pos", 0))

    json.dump({"list": target, "cards": cards}, sys.stdout, indent=2, ensure_ascii=False)
    print()


if __name__ == "__main__":
    main()
