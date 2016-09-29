#include "entry.h"
#include <QLineEdit>
#include <QTextEdit>
#include <QWidget>
#include <QDialog>
#include <QPushButton>
#include <iostream>

Entry::Entry(QDialog *parent)
    : QDialog(parent)
{
    setLayout(this->frm);
}

void Entry::populate() {
    QTextEdit *notes = new QTextEdit(this);
    QLineEdit *tags = new QLineEdit(this);
    QPushButton *closeBtn = new QPushButton("Close", this);
    QPushButton *submitBtn = new QPushButton("Submit", this);
    closeBtn->setFixedSize(157, 23);
    submitBtn->setFixedSize(157, 23);
    this->frm->addRow("Notes:", notes);
    this->frm->addRow("Tags (separated by commas):", tags);
    this->frm->addRow(closeBtn, submitBtn);
}

Entry::~Entry() {}
