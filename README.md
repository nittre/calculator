test1
import json
import os
from datetime import datetime

DATA_FILE = "account_book.json"

class AccountBook:
    def __init__(self):
        self.records = []
        self.load_data()

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                self.records = json.load(f)
        else:
            self.records = []

    def save_data(self):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(self.records, f, ensure_ascii=False, indent=4)

    def add_record(self, record_type, amount, category, memo):
        record = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "type": record_type,
            "amount": amount,
            "category": category,
            "memo": memo
        }
        self.records.append(record)
        self.save_data()
        print("✅ 입력 완료!")

    def show_records(self):
        if not self.records:
            print("📂 기록이 없습니다.")
            return
        
        print("\n===== 전체 내역 =====")
        for i, record in enumerate(self.records):
            print(f"[{i}] {record['date']} | {record['type']} | "
                  f"{record['amount']}원 | {record['category']} | {record['memo']}")

    def delete_record(self, index):
        if 0 <= index < len(self.records):
            deleted = self.records.pop(index)
            self.save_data()
            print(f"🗑 삭제 완료: {deleted}")
        else:
            print("❌ 잘못된 번호입니다.")

    def show_balance(self):
        balance = 0
        for record in self.records:
            if record["type"] == "수입":
                balance += record["amount"]
            else:
                balance -= record["amount"]
        print(f"💰 현재 잔액: {balance}원")

    def monthly_summary(self):
        summary = {}
        for record in self.records:
            month = record["date"][:7]
            if month not in summary:
                summary[month] = 0
            if record["type"] == "수입":
                summary[month] += record["amount"]
            else:
                summary[month] -= record["amount"]

        print("\n===== 월별 잔액 =====")
        for month, total in summary.items():
            print(f"{month}: {total}원")


def main():
    book = AccountBook()

    while True:
        print("\n===== 가계부 메뉴 =====")
        print("1. 수입 입력")
        print("2. 지출 입력")
        print("3. 전체 조회")
        print("4. 삭제")
        print("5. 잔액 확인")
        print("6. 월별 합계")
        print("0. 종료")

        choice = input("선택: ")

        if choice == "1":
            amount = int(input("금액: "))
            category = input("카테고리: ")
            memo = input("메모: ")
            book.add_record("수입", amount, category, memo)

        elif choice == "2":
            amount = int(input("금액: "))
            category = input("카테고리: ")
            memo = input("메모: ")
            book.add_record("지출", amount, category, memo)

        elif choice == "3":
            book.show_records()

        elif choice == "4":
            book.show_records()
            index = int(input("삭제할 번호: "))
            book.delete_record(index)

        elif choice == "5":
            book.show_balance()

        elif choice == "6":
            book.monthly_summary()

        elif choice == "0":
            print("프로그램 종료 👋")
            break

        else:
            print("❌ 잘못된 입력입니다.")


if __name__ == "__main__":
    main()",
   
}
