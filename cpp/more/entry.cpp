#include "entry.h"
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
    closeBtn->setFixedSize(157, 23);
    submitBtn->setFixedSize(157, 23);
    this->frm->addRow("Notes:", notes);
    this->frm->addRow("Tags (separated by commas):", tags);
    this->frm->addRow(closeBtn, submitBtn);

    connect(closeBtn, SIGNAL(clicked()), this, SLOT(close()));
    // connect(submitBtn, SIGNAL(clicked()), this, SLOT(processData()));
}

Entry::~Entry() {}
