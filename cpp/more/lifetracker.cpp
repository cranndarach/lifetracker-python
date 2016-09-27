#include <QGridLayout>
#include <QPushButton>
#include <QMainWindow>
#include <QTabWidget>
#include "lifetracker.h"

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
    QList<QString> mainBtnNames;
    QList<QString> inflBtnNames;
    QList<QString> statusBtnNames;
    mainBtnNames << "Log Event" << "Log Task" << "Log EXP"
                 << "Simple Entry" << "Generic Entry";
    inflBtnNames << "Log Sleep" << "Log Coping Mechanism" << "Log Medicine Taken"
                 << "Misc. Influence";
    statusBtnNames << "Log Spoons" << "Log Mood" << "Log Health/Symptoms"
                   << "Log Pain Level" << "Log Mobility" << "Log hunger"
                   << "Log Headache";

    // Add the buttons to the pages
    // (make it pretty some other time)
    // int pos = 0;
    // for (int page=0; page<3; page++){}
    for (int posn=0; posn<5; posn++) {
        // is there a way to set the row length in advance, and
        // with each "addWidget()", assume it's going in the next
        // column, or moving onto the next row?
        QPushButton *btn = new QPushButton(mainBtnNames[posn], mainTab);
        btn->setFixedSize(157, 23);
        mainGrid->addWidget(btn, posn/3, posn%3);
    }
    // posn = 0;
    for (int posn2=0; posn2<4; posn2++) {
        QPushButton *btn = new QPushButton(inflBtnNames[posn2], inflTab);
        btn->setFixedSize(157, 23);
        inflGrid->addWidget(btn, posn2/3, posn2%3);
    }
    // posn = 0;
    for (int posn3=0; posn3<7; posn3++) {
        QPushButton *btn = new QPushButton(statusBtnNames[posn3], statusTab);
        btn->setFixedSize(157, 23);
        statusGrid->addWidget(btn, posn3/3, posn3%3);
    }

    // Set the central frame widget as a central widget
    setCentralWidget(central);
    // setLayout(mainGrid);
    // setLayout(inflGrid);
    // setLayout(statusGrid);
}
