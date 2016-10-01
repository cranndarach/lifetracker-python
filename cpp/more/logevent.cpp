#include "logevent.h"
#include <iostream>
#include <fstream>
#include <QUuid>
#include <QMessageBox>

LogEvent::LogEvent(Entry *parent)
    : Entry(parent)
{
    this->frm->addRow("Title:", title);
    // connect(this->submitBtn, SIGNAL(clicked()), this->data, SLOT(insert(title->value())));
    this->frm->addRow("Category:", category);
    this->frm->addRow("Start:", startDT);
    this->frm->addRow("End:", endDT);
    this->frm->addRow("Location:", location);
    this->frm->addRow("Mood:", mood);
    this->frm->addRow("Spoons:", spoons);

    populate();
    // connect(this->submitBtn, SIGNAL(clicked()), this, SLOT(submit()));
}

void LogEvent::serialize() {
    uuid = QUuid::createUuid().toString();
    d.insert("uuid", QJsonValue(uuid));
    d.insert("title", QJsonValue(this->title->text()));
    d.insert("category", QJsonValue(this->category->text()));
    d.insert("startDT", QJsonValue(this->startDT->dateTime().toString()));
    d.insert("endDT", QJsonValue(this->endDT->dateTime().toString()));
    d.insert("location", QJsonValue(this->location->text()));
    d.insert("mood", QJsonValue(this->mood->value()));
    d.insert("spoons", QJsonValue(this->spoons->value()));
    d.insert("notes", QJsonValue(this->notes->toPlainText()));
    d.insert("tags", QJsonValue(this->tags->text()));
}

// void LogEvent::processData() {
//     QJsonObject d; // = new QJsonObject();
//     QString uuid = QUuid::createUuid().toString();
//     d.insert("uuid", QJsonValue(uuid));
//     d.insert("title", QJsonValue(this->title->text()));
//     d.insert("category", QJsonValue(this->category->text()));
//     d.insert("startDT", QJsonValue(this->startDT->dateTime().toString()));
//     d.insert("endDT", QJsonValue(this->endDT->dateTime().toString()));
//     d.insert("location", QJsonValue(this->location->text()));
//     d.insert("mood", QJsonValue(this->mood->value()));
//     d.insert("spoons", QJsonValue(this->spoons->value()));
//     d.insert("notes", QJsonValue(this->notes->toPlainText()));
//     d.insert("tags", QJsonValue(this->tags->text()));
//
//     Preferences p;
//     QString saveLoc = p.getSaveLoc();
//     QString filepath = saveLoc + "/data-" + uuid + ".json";
//     QFile dataFile(filepath);
//     if (!dataFile.open(QIODevice::WriteOnly | QIODevice::Text)) {
//         std::cout << "File not open" << std::endl;
//         return;
//     }
//     QJsonDocument saveData(d);
//     dataFile.write(saveData.toJson());
//     dataFile.close();
// }

LogEvent::~LogEvent() {}
