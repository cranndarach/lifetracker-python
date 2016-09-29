#ifndef LOGMEDS_H
#define LOGMEDS_H

#include "entry.h"

class LogMeds: public Entry {
public:
    // explicit
    LogMeds(Entry *parent = 0);
    ~LogMeds(); // destructor
};


#endif // LOGMEDS_H
