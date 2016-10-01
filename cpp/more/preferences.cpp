#include "preferences.h"
#include <QDir>
#include <QString>

Preferences::Preferences() {
    setSaveLoc();
}

void Preferences::setSaveLoc()
{
    // Eventually make it reference a file with settings which stores the value
    // of saveLoc. On first use (or if no settings file exists), prompt user for
    // preference(s).
    QString home = QDir::homePath();
    saveLoc = home + "/lifetracker-data";
    QDir saveDir(saveLoc);
    if (!saveDir.exists()) {
        saveDir.mkdir(saveLoc);
    }
}
QString Preferences::getSaveLoc()
{
    return saveLoc;
}

Preferences::~Preferences() {}
