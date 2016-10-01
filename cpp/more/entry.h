#ifndef ENTRY_H
#define ENTRY_H

#include <QDialog>
#include <QFormLayout>
#include <QLineEdit>
#include <QTextEdit>
#include <QJsonObject>
#include <QPushButton>
#include <fstream>
#include <iostream>

class Entry: public QDialog
{
Q_OBJECT

public:
    Entry(QDialog *parent = 0);
    ~Entry(); // destructor
    QString uuid;
    QJsonObject d;
    void populate();
    void saveData();
    virtual void serialize();
    QFormLayout *frm = new QFormLayout(this);
    QTextEdit *notes = new QTextEdit(this);
    QLineEdit *tags = new QLineEdit(this);
    QPushButton *closeBtn = new QPushButton("Close", this);
    QPushButton *submitBtn = new QPushButton("Submit", this);

public slots:
    void submit();

private:

};

#endif // ENTRY_H
