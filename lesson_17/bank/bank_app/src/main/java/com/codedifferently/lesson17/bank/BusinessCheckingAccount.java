package com.codedifferently.lesson17.bank;

import java.util.Set;

public class BusinessCheckingAccount extends CheckingAccount {

  /**
   * Creates a new Business Checking account.
   *
   * @param accountNumber The account number.
   * @param owners The owners of the account; at least one must be a business account
   * @param initialBalance The initial balance of the account.
   */
  BusinessCheckingAccount(String accountNumber, Set<Customer> owners, double initialBalance) {
    super(accountNumber, validateBusinessOwner(owners), initialBalance);
  }

  private static Set<Customer> validateBusinessOwner(Set<Customer> owners) {
    boolean hasBusinessOwner = owners.stream().anyMatch(Customer::isBusinessAccount);
    if (!hasBusinessOwner) {
      throw new IllegalArgumentException("At least one owner must be a business.");
    }
    return owners;
  }
}
