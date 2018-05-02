MailboxApi mailbox = new MailboxApi(mailbox, apikey);

Email[] emails =
mailbox.getEmailsByRecipient("anything.yourkey@mailosaur.in");

assertEquals("The subject should be set",
             "Reset your password", emails[0].Subject);