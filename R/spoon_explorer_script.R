require(plyr)
require(knitr)
source("lifetracker_functions.R")

#### Edit file path as needed ####
d <- read.csv("2016-09-15.csv", stringsAsFactors = F)
#### ------------------------ ####

day <- d[ , c("when_hour", "when_minute", "when_ampm", "spoons", "start_hour", 
              "start_minute", "start_ampm", "start_spoons", "end_hour", "end_minute", 
              "end_ampm", "end_spoons")]
# Convert "when" etc. to 24-hour, and then to proportions:
day$when_hprop <- hprop(day$when_hour, day$when_minute, day$when_ampm)
day$start_hprop <- hprop(day$start_hour, day$start_minute, day$start_ampm)
day$end_hprop <- hprop(day$end_hour, day$end_minute, day$end_ampm)
# Same for sleep:
day$s_start_hprop <- hprop(d$sleep_start_hour, d$sleep_start_minute, d$sleep_start_ampm)
day$s_end_hprop <- hprop(d$sleep_end_hour, d$sleep_end_minute, d$sleep_end_ampm)
day$s_duration <- ifelse(day$s_end_hprop > day$s_start_hprop, 
                         day$s_end_hprop - day$s_start_hprop, 
                         (day$s_end_hprop + 24) - day$s_start_hprop)

# Smush dates into single string, add to single column:
day$start_date <- makedate(d$start_month, d$start_day, d$start_year)
day$end_date <- makedate(d$end_month, d$end_day, d$end_year)
day$sleep_date <- makedate(d$sleep_end_month, d$sleep_end_day, d$sleep_end_year)
day$when_date <- makedate(d$when_month, d$when_day, d$when_year)
day$date <- rep(NA, dim(day)[1])
day$date <- ifelse(day$end_date != "NA/NA/NA", day$end_date, 
                   ifelse(day$when_date != "NA/NA/NA", day$when_date, 
                          ifelse(day$sleep_date != "NA/NA/NA", day$sleep_date, day$date)))

# Fill in sleep duration for each date:
sleepdate <- day[!(is.na(day$s_duration)), c("date", "s_duration")]
names(sleepdate)[2] <- "sleepdur"
day <- join(day, sleepdate, by="date")
# Fill in wakeup time for each date:
wakeup <- day[!(is.na(day$s_end_hprop)), c("date", "s_end_hprop")]
names(wakeup)[2] <- "wakeup"
day <- join(day, wakeup, by="date")
day$when <- ifelse(!(is.na(day$when_hprop)), day$when_hprop,
                   ifelse(!is.na(day$end_hprop), day$end_hprop, NA))
# Calculate time awake:
day$since_wakeup <- day$when - day$wakeup

# Put relevant variables into a df for regression:
# Vectors for time, and corresponding vectors for spoons:
combo.time <- c(day$start_hprop, day$end_hprop, day$when_hprop)
combo.spoons <- c(day$start_spoons, day$end_spoons, day$spoons)
# Make the data frame:
combo <- data.frame("Time"=combo.time, "Spoons"=combo.spoons, "Sleep"=rep(day$sleepdur, 3),
                    "SinceWakeup"=rep(day$since_wakeup, 3))
# Clean it:
combo <- combo[!is.na(combo$Time) & !is.na(combo$Spoons) & !is.na(combo$Sleep), ]
combo <- combo[order(combo$Time), ]
combo <- combo[combo$Spoons != 0, ]
combo <- combo[combo$SinceWakeup > 0, ] # idk, take care of this later
combo <- combo[combo$Sleep < 12, ] # get rid of accidental "pm"s or whatever
combo$Time <- ifelse(combo$Time < 6, combo$Time + 24, combo$Time)

# Scatterplot spoons vs. time awake:
plot(combo$SinceWakeup, combo$Spoons, xlab="Time since waking up (hours)", 
     ylab="Spoons", main="Spoons with respect to time since waking up", col="plum3", lwd=3)

# Run the regression:
spoons.wakeup.m1 <- lm(Spoons ~ SinceWakeup, combo) # Step 1: main effect of time awake
spoons.wakeup.m2 <- update(spoons.wakeup.m1, ~ . + SinceWakeup/Sleep) # Step 2: add interaction with sleep
kable(anova(spoons.wakeup.m1, spoons.wakeup.m2))

# Add line to plot for main effect of time awake:
abline(spoons.wakeup.m1, col="navyblue", lwd=2)

# Add lines for interaction:

# Simple slopes analysis:
coefmat <- summary(spoons.wakeup.m2)$"coefficients"
ests <- coefmat[,1]
b.t <- ests["SinceWakeup"]
b.int <- ests["SinceWakeup:Sleep"]
a <- ests[1]
# treat sleep as the moderator
# points include the mean (0), and +/- 1 sd
low.slp <- mean(combo$Sleep) - sd(combo$Sleep)
high.slp <- mean(combo$Sleep) + sd(combo$Sleep)
mid.slp <- mean(combo$Sleep)
# intercept in simple slopes analysis: a + b2*x2
# If no main effect of x2...ignore it? Come back to this
low.a <- a #+ low.slp
high.a <- a #+ high.slp
mid.a <- a
# b in simple slopes: b1 + b3x2
low.b <- b.t + b.int*low.slp
high.b <- b.t + b.int*high.slp
mid.b <- b.t

# Plot the lines:
abline(low.a,low.b,xlim=c(min(combo$SinceWakeup),max(combo$SinceWakeup)),col="red2", lwd=2)
abline(high.a,high.b,xlim=c(min(combo$SinceWakeup),max(combo$SinceWakeup)),col="green3", lwd=2)
abline(a,b.t,xlim=c(min(combo$SinceWakeup),max(combo$SinceWakeup)),col="goldenrod1", lwd=2)
legend(12, 83, legend=c("Low", "Medium", "High", "Unmoderated"), lty=c(1,1), lwd=2.5, 
       col=c("red2", "goldenrod1", "green3", "navyblue"), title="Amount of sleep")




