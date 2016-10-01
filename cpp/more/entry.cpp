#include "entry.h"
#include "preferences.h"
#include <QWidget>
#include <QDialog>
#include <QPushButton>
#include <QJsonObject>
#include <QJsonDocument>
#include <QJsonValue>
#include <QFile>
#include <QMessageBox>
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
    connect(submitBtn, SIGNAL(clicked()), this, SLOT(submit()));
}
void Entry::serialize() {}
void Entry::saveData() {
    Preferences p;
    QString saveLoc = p.getSaveLoc();
    QString filepath = saveLoc + "/data-" + uuid + ".json";
    QFile dataFile(filepath);
    if (!dataFile.open(QIODevice::WriteOnly | QIODevice::Text)) {
        std::cout << "File not open" << std::endl;
        return;
    }
    QJsonDocument saveData(d);
    dataFile.write(saveData.toJson());
    dataFile.close();
}
void Entry::submit() {
    serialize();
    saveData();
    QMessageBox *success = new QMessageBox(this);
    success->setWindowTitle("Success");
    success->setText("Your entry has been saved.");
    success->setStandardButtons(QMessageBox::Ok);
    success->setDefaultButton(QMessageBox::Ok);
    success->exec();
}

Entry::~Entry() {}
