#include <QCoreApplication>
#include <QGridLayout>
#include <QPushButton>
#include <QMainWindow>
#include <QTabWidget>
#include <QString>
#include "lifetracker.h"
#include "logevent.h"
#include "logtask.h"
#include "logexp.h"
#include "logsimple.h"
#include "logsleep.h"

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

    // Create the buttons
    QPushButton *bEvent = new QPushButton("Log Event", this);
    QPushButton *bTask = new QPushButton("Log Task", this);
    QPushButton *bExp = new QPushButton("Log EXP Gained", this);
    QPushButton *bSimple = new QPushButton("Simple Entry", this);
    QPushButton *bGeneric = new QPushButton("Generic Entry", this);

    QPushButton *bSleep = new QPushButton("Log Sleep", this);
    QPushButton *bCopech = new QPushButton("Log Coping Mechanism", this);
    QPushButton *bMeds = new QPushButton("Log Medicine Taken", this);
    QPushButton *bMiscInfl = new QPushButton("Misc. Influence", this);

    QPushButton *bSpoons = new QPushButton("Log Spoons", this);
    QPushButton *bMood = new QPushButton("Log Mood", this);
    QPushButton *bHealth = new QPushButton("Log Health/Symptoms", this);
    QPushButton *bPain = new QPushButton("Log Pain Levels", this);
    QPushButton *bMobility = new QPushButton("Log Mobility", this);
    QPushButton *bHunger = new QPushButton("Log Hunger", this);
    QPushButton *bHeadache = new QPushButton("Log Headache", this);

    // Make an array of buttons for each tab
    QPushButton *mainBtns[] = {bEvent, bTask, bExp, bSimple, bGeneric};
    QPushButton *inflBtns[] = {bSleep, bCopech, bMeds, bMiscInfl};
    QPushButton *statusBtns[] = {bSpoons, bMood, bHealth, bPain, bMobility, bHunger, bHeadache};

    // Iterate through and put them in the grid
    // (change the "posnX<Y" if adding more buttons)
    for (int posn=0; posn<5; posn++) {
        mainBtns[posn]->setFixedSize(157, 23);
        mainGrid->addWidget(mainBtns[posn], posn/3, posn%3);
    }
    for (int posn2=0; posn2<4; posn2++) {
        inflBtns[posn2]->setFixedSize(157, 23);
        inflGrid->addWidget(inflBtns[posn2], posn2/3, posn2%3);
    }
    for (int posn3=0; posn3<7; posn3++) {
        statusBtns[posn3]->setFixedSize(157, 23);
        statusGrid->addWidget(statusBtns[posn3], posn3/3, posn3%3);
    }

    connect(bEvent, SIGNAL(released()), this, SLOT(on_bEvent_clicked()));
    connect(bTask, SIGNAL(released()), this, SLOT(on_bTask_clicked()));
    connect(bExp, SIGNAL(released()), this, SLOT(on_bExp_clicked()));
    connect(bSimple, SIGNAL(released()), this, SLOT(on_bSimple_clicked()));

    connect(bSleep, SIGNAL(released()), this, SLOT(on_bSleep_clicked()));

    // Set the central frame widget as a central widget
    setCentralWidget(central);
}

// Slots: receive a button click, create corresponding form
void Lifetracker::on_bEvent_clicked()
{
    // LogEvent e;
    e->setWindowTitle("Log Event");
    e->exec();
}
void Lifetracker::on_bTask_clicked()
{
    // LogTask t;
    t->setWindowTitle("Log Task");
    t->exec();
}
void Lifetracker::on_bExp_clicked()
{
    // LogExp x;
    x->setWindowTitle("Log EXP Gained");
    x->exec();
}
void Lifetracker::on_bSimple_clicked()
{
    // LogSimple s;
    s->setWindowTitle("Simple Entry");
    s->exec();
}
void Lifetracker::on_bSleep_clicked()
{
    // LogSleep sl;
    sl->setWindowTitle("Log Sleep");
    sl->exec();
}

Lifetracker::~Lifetracker() {}
