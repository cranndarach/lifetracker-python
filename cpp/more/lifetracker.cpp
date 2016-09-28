#include <QGridLayout>
#include <QPushButton>
#include <QMainWindow>
#include <QTabWidget>
#include <QString>
#include "lifetracker.h"
#include "logevent.h"

Lifetracker::Lifetracker(QMainWindow *parent)
    : QMainWindow(parent)
{
    // Make a frame for the rest of the widgets to reside in
    QWidget *central = new QWidget(this);

    // Make a "notebook" as a child to the central frame widget
    QTabWidget *tabs = new QTabWidget(central);
    // Make tab-precursors
    QWidget *mainTab = new QWidget();
    QWidget *inflTab = new QWidget();
    QWidget *statusTab = new QWidget();

    // Add them to the notebook
    tabs->addTab(mainTab, "Main");
    tabs->addTab(inflTab, "Influences");
    tabs->addTab(statusTab, "Status");

    // Give them grid layouts
    QGridLayout *mainGrid = new QGridLayout(mainTab);
    QGridLayout *inflGrid = new QGridLayout(inflTab);
    QGridLayout *statusGrid = new QGridLayout(statusTab);
    mainGrid->setSpacing(2);
    inflGrid->setSpacing(2);
    statusGrid->setSpacing(2);

    // Make lists of button names
    // QList<QString> mainBtnNames;
    // QList<QString> inflBtnNames;
    // QList<QString> statusBtnNames;
    // mainBtnNames << "Log Event" << "Log Task" << "Log EXP"
    //              << "Simple Entry" << "Generic Entry";
    // inflBtnNames << "Log Sleep" << "Log Coping Mechanism" << "Log Medicine Taken"
    //              << "Misc. Influence";
    // statusBtnNames << "Log Spoons" << "Log Mood" << "Log Health/Symptoms"
    //                << "Log Pain Level" << "Log Mobility" << "Log hunger"
    //                << "Log Headache";

    QPushButton *bEvent = new QPushButton("Log Event");    // addButton("Log Event", mainTab, mainGrid, this->mainPosn);
    QPushButton *bTask = new QPushButton("Log Task");     // addButton("Log Task", mainTab, mainGrid, this->mainPosn);
    QPushButton *bExp = new QPushButton("Log EXP Gained");      // addButton("Log EXP", mainTab, mainGrid, this->mainPosn);
    QPushButton *bSimple = new QPushButton("Simple Entry");   // addButton("Simple Entry", mainTab, mainGrid, this->mainPosn);
    QPushButton *bGeneric = new QPushButton("Generic Entry");  // addButton("Generic Entry", mainTab, mainGrid, this->mainPosn);

    QPushButton *bSleep = new QPushButton("Log Sleep");    // addButton("Log Sleep", inflTab, inflGrid, this->inflPosn);
    QPushButton *bCopech = new QPushButton("Log Coping Mechanism");   // addButton("Log Coping Mechanism", inflTab, inflGrid, this->inflPosn);
    QPushButton *bMeds = new QPushButton("Log Medicine Taken");     // addButton("Log Medicine Taken", inflTab, inflGrid, this->inflPosn);
    QPushButton *bMiscInfl = new QPushButton("Misc. Influence"); // addButton("Misc. Influence", inflTab, inflGrid, this->inflPosn);

    QPushButton *bSpoons = new QPushButton("Log Spoons");   // addButton("Log Spoons", statusTab, statusGrid, this->statusPosn);
    QPushButton *bMood = new QPushButton("Log Mood");     // addButton("Log Mood", statusTab, statusGrid, this->statusPosn);
    QPushButton *bHealth = new QPushButton("Log Health/Symptoms");   // addButton("Log Health/Symptoms", statusTab, statusGrid, this->statusPosn);
    QPushButton *bPain = new QPushButton("Log Pain Levels");     // addButton("Log Pain Level", statusTab, statusGrid, this->statusPosn);
    QPushButton *bMobility = new QPushButton("Log Mobility"); // addButton("Log Mobility", statusTab, statusGrid, this->statusPosn);
    QPushButton *bHunger = new QPushButton("Log Hunger");   // addButton("Log Hunger", statusTab, statusGrid, this->statusPosn);
    QPushButton *bHeadache = new QPushButton("Log Headache"); // addButton("Log Headache", statusTab, statusGrid, this->statusPosn);

    QPushButton *mainBtns[] = {bEvent, bTask, bExp, bSimple, bGeneric};
    QPushButton *inflBtns[] = {bSleep, bCopech, bMeds, bMiscInfl};
    QPushButton *statusBtns[] = {bSpoons, bMood, bHealth, bPain, bMobility, bHunger, bHeadache};

    // Add the buttons to the pages
    // (make it pretty some other time)
    // int pos = 0;
    // for (int page=0; page<3; page++){}
    for (int posn=0; posn<5; posn++) {
        // QPushButton *btn = new QPushButton(mainBtnNames[posn], mainTab);
        mainBtns[posn]->setFixedSize(157, 23);
        mainGrid->addWidget(mainBtns[posn], posn/3, posn%3);
    }
    // posn = 0;
    for (int posn2=0; posn2<4; posn2++) {
        // QPushButton *btn = new QPushButton(inflBtnNames[posn2], inflTab);
        inflBtns[posn2]->setFixedSize(157, 23);
        inflGrid->addWidget(inflBtns[posn2], posn2/3, posn2%3);
    }
    // posn = 0;
    for (int posn3=0; posn3<7; posn3++) {
        // QPushButton *btn = new QPushButton(statusBtnNames[posn3], statusTab);
        statusBtns[posn3]->setFixedSize(157, 23);
        statusGrid->addWidget(statusBtns[posn3], posn3/3, posn3%3);
    }

    // Set the central frame widget as a central widget
    setCentralWidget(central);
}

// QPushButton* Lifetracker::addButton(QString label, QWidget *tab, QGridLayout *grid, int posn) {
//     //QPushButton *btn = new QPushButton(label, tab);
//     btn->setFixedSize(157, 23);
//     grid->addWidget(btn, posn/3, posn%3);
//     posn++;
//     //return btn;
// }

void Lifetracker::on_bEvent_clicked()
{
    LogEvent e;
    e.exec();
}
