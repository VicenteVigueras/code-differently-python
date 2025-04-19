package com.codedifferently.lesson17.bank;

public class MoneyOrder {

  private String moneyOrderNumber;
  private double amount;
  private BankAccount bankAccount;

  /**
   * Creates MoneyOrder
   *
   * @param moneyOrderNumber The Money Order number
   * @param amount The amount of the money order
   * @param bankAccount The account the money order is drawn from
   */
  public MoneyOrder(String moneyOrderNumber, double amount, BankAccount bankAccount) {
    this.moneyOrderNumber = moneyOrderNumber;
    this.amount = amount;
    this.bankAccount = bankAccount;
    bankAccount.withdraw(amount);
  }

  @Override
  public String toString() {
    return "MoneyOrder{"
            + "moneyOrderNumber='"
            + moneyOrderNumber
            + '\''
            + ", amount="
            + amount
            + ", account="
            + bankAccount.getAccountNumber()
            + '}';
  }
}
