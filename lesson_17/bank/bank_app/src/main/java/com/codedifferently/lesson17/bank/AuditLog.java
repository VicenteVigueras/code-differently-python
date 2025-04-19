package com.codedifferently.lesson17.bank;

import ch.qos.logback.classic.Logger;
import org.slf4j.LoggerFactory;

public class AuditLog {

  private static final Logger logger = (Logger) LoggerFactory.getLogger(AuditLog.class);

  public void record(String record) {
    logger.info(record);
  }
}
