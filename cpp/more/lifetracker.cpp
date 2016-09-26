#include <QGridLayout>
#include <QPushButton>
#include "lifetracker.h"

Lifetracker::Lifetracker(QWidget *parent)
    : QWidget(parent)
{
    QGridLayout *grid = new QGridLayout(this);
    grid->setSpacing(2);

    QList<QString> btnNames; //({ "Log Event", "Log Task", "Log EXP",
        // "Simple Entry", "Generic Entry"
    // });
    btnNames << "Log Event" << "Log Task" << "Log EXP" << "Simple Entry" << "Generic Entry";

    //int pos = 0;

    for (int pos=0; pos<5; pos++) {
        QPushButton *btn = new QPushButton(btnNames[pos], this);
        btn->setFixedSize(157, 23);
        grid->addWidget(btn, pos/3, pos%3);
    }

    setLayout(grid);
}
