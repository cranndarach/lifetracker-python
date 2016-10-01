#ifndef PREFERENCES_H
#define PREFERENCES_H

#include <QString>
#include <QDir>

class Preferences {

public:
    Preferences();
    ~Preferences(); //destructor
    QString getSaveLoc();

private:
    QString saveLoc;
    void setSaveLoc();
};

#endif // PREFERENCES_H
