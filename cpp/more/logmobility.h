#ifndef LOGMOBILITY_H
#define LOGMOBILITY_H

#include "entry.h"

class LogMobility: public Entry {
public:
    // explicit
    LogMobility(Entry *parent = 0);
    ~LogMobility(); // destructor
};


#endif // LOGMOBILITY_H
