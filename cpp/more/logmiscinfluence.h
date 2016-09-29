#ifndef LOGMISCINFLUENCE_H
#define LOGMISCINFLUENCE_H

#include "entry.h"

class LogMiscInfluence: public Entry {
public:
    // explicit
    LogMiscInfluence(Entry *parent = 0);
    ~LogMiscInfluence(); // destructor
};


#endif // LOGMISCINFLUENCE_H
