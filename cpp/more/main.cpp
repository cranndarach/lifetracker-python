#include <QApplication>
#include "lifetracker.h"
#include "entry.cpp"

int main(int argc, char *argv[]) {

    QApplication app(argc, argv);

    Lifetracker w;

    w.resize(500, 250);
    w.setWindowTitle("LifeTracker");
    w.show();

    return app.exec();
}