#include "logevent.h"
#include <iostream>
#include <fstream>
#include <QUuid>
#include <QMessageBox>

LogEvent::LogEvent(Entry *parent)
    : Entry(parent)
{
    this->frm->addRow("Title:", title);
    this->frm->addRow("Category:", category);
    this->frm->addRow("Start:", startDT);
    this->frm->addRow("End:", endDT);
    this->frm->addRow("Location:", location);
    this->frm->addRow("Mood:", mood);
    this->frm->addRow("Spoons:", spoons);

    populate();
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

LogEvent::~LogEvent() {}
