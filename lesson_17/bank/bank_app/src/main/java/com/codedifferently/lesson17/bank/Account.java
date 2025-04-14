package com.codedifferently.lesson17.bank;

import java.util.Set;

import com.codedifferently.lesson17.bank.exceptions.InsufficientFundsException;

public interface Account {
   
  /**
   * Gets the account number.
   *
   * @return The account number.
   */
  public String getAccountNumber();

  /**
   * Gets the owners of the account.
   *
   * @return The owners of the account.
   */
  public Set<Customer> getOwners();

  /**
   * Deposits funds into the account.
   *
   * @param amount The amount to deposit.
   */
  public void deposit(double amount) throws IllegalStateException;

  /**
   * Withdraws funds from the account.
   *
   * @param amount
   * @throws InsufficientFundsException
   */
  public void withdraw(double amount) throws InsufficientFundsException;

  /**
   * Gets the balance of the account.
   *
   * @return The balance of the account.
   */
  public double getBalance();
  /** Closes the account. */
  
  public void closeAccount();
  /**
   * Checks if the account is closed.
   *
   * @return True if the account is closed, otherwise false.
   */
  public boolean isClosed();
 
}


