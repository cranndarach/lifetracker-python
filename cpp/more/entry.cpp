#include "entry.h"
#include <QFormLayout>
#include <QLineEdit>
#include <QTextEdit>
#include <QWidget>
#include <QDialog>
#include <QPushButton>
#include <iostream>

Entry::Entry(QDialog *parent):
    QDialog(parent)
{
    // QFormLayout *frm = new QFormLayout(this);

    setLayout(this::frm);
}

template <class T>
void Entry::addLine(std::string label, T *ent) {
    // Make a widget of the given type
    // T *ent = new T(this);
    // Add to form with label
    this::frm->addRow(label, ent);
    /// it doesn't like the this:: but i'm going to bed
}

void Entry::populate() {
    QTextEdit *notes = new QTextEdit(this);
    QLineEdit *tags = new QLineEdit(this);
    QPushButton *closeBtn = new QPushButton(this);
    QPushButton *submitBtn = new QPushButton(this);
    this::frm->addRow("Notes:", notes);
    this::frm->addRow("Tags (separated by commas):", tags);
    this::frm->addRow(closeBtn, submitBtn);
}
