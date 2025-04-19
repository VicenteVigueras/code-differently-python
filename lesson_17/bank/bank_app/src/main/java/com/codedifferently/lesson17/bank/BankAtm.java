package com.codedifferently.lesson17.bank;

import com.codedifferently.lesson17.bank.exceptions.AccountNotFoundException;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.UUID;

/** Represents a bank ATM. */
public class BankAtm {

  private final Map<UUID, Customer> customerById = new HashMap<>();
  private final Map<String, BankAccount> accountByNumber = new HashMap<>();
  private final AuditLog auditLog = new AuditLog();

  /**
   * Adds a bank account to the bank.
   *
   * @param account The account to add.
   */
  public void addAccount(BankAccount account) {
    accountByNumber.put(account.getAccountNumber(), account);
    account
        .getOwners()
        .forEach(
            owner -> {
              customerById.put(owner.getId(), owner);
            });
    auditLog.record("The account " + account.toString() + " has been added");
  }

  /**
   * Finds all accounts owned by a customer.
   *
   * @param customerId The ID of the customer.
   * @return The unique set of accounts owned by the customer.
   */
  public Set<BankAccount> findAccountsByCustomerId(UUID customerId) {
    return customerById.containsKey(customerId)
        ? customerById.get(customerId).getAccounts()
        : Set.of();
  }

  /**
   * Deposits funds into an account.
   *
   * @param accountNumber The account number.
   * @param amount The amount to deposit.
   */
  public void depositFunds(String accountNumber, double amount) {
    BankAccount account = getAccountOrThrow(accountNumber);
    account.deposit(amount);
    auditLog.record("The amount " + amount + " has been deposited into " + account.toString());
  }

  /**
   * Deposits funds into an account using a check.
   *
   * @param accountNumber The account number.
   * @param check The check to deposit.
   */
  public void depositFunds(String accountNumber, Check check) {
    BankAccount account = getAccountOrThrow(accountNumber);
    check.depositFunds(account);
    auditLog.record(
        "The check " + check.toString() + " has been deposited into " + account.toString());
  }

  /**
   * Withdraws funds from an account.
   *
   * @param accountNumber The account number
   * @param amount The amount to be withdrawn
   */
  public void withdrawFunds(String accountNumber, double amount) {
    BankAccount account = getAccountOrThrow(accountNumber);
    account.withdraw(amount);
    auditLog.record("The amount " + amount + " has been withdrawn from " + account.toString());
  }

  /**
   * Gets an account by its number or throws an exception if not found.
   *
   * @param accountNumber The account number.
   * @return The account.
   */
  private BankAccount getAccountOrThrow(String accountNumber) {
    BankAccount account = accountByNumber.get(accountNumber);
    if (account == null || account.isClosed()) {
      throw new AccountNotFoundException("Account not found");
    }
    return account;
  }
}
