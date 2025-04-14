package com.codedifferently.lesson17.bank;

import java.util.Set;

public class BusinessCheckingAccount extends CheckingAccount {

  BusinessCheckingAccount(String accountNumber, Set<Customer> owners, double initialBalance) {
    super(accountNumber, owners, initialBalance);

    boolean hasBusinessOwner = owners.stream().anyMatch(Customer::isBusinessAccount);

    if (!hasBusinessOwner) {
      throw new IllegalArgumentException("At least one owner must be a business.");
    }
  }
}
