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
public:
    Entry(QDialog *parent = 0);
    ~Entry(); // destructor
    void populate();
    // void sendData();
    // virtual void processData();
    // void processData();
    // void saveData();
    // void count();
    QFormLayout *frm = new QFormLayout(this);
    QTextEdit *notes = new QTextEdit(this);
    QLineEdit *tags = new QLineEdit(this);
    QPushButton *closeBtn = new QPushButton("Close", this);
    QPushButton *submitBtn = new QPushButton("Submit", this);
    // QJsonObject *data = new QJsonObject(this);

private:

};

#endif // ENTRY_H
