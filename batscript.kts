/*
 * This is a script written using Kotlin for checking the current
 * battery status. To run it, execute:
 *    kotlinc -script batscript.kts
 *
 * It parses the information in /sys/class/power_supply/BAT0 to get the
 * current battery state. It outputs this information in the standard
 * i3blocks format.
 *
 * Author: Kyle Laker<kyle@laker.email>
 * Licensed under the MIT License (see the LICENSE file for details)
 */

import java.nio.file.*
import kotlin.system.exitProcess


val batteryDirectory = "/sys/class/power_supply/BAT0/"
val capacityFile = Paths.get("$batteryDirectory/charge_full")
val chargeFile = Paths.get("$batteryDirectory/charge_now")
val statusFile = Paths.get("$batteryDirectory/status")

val capacityIn = Files.newBufferedReader(capacityFile)
val chargeIn = Files.newBufferedReader(chargeFile)
val statusIn = Files.newBufferedReader(statusFile)

val capacity = capacityIn.readLine().toDouble()
val charge = chargeIn.readLine().toDouble()
val status = statusIn.readLine()

val percent = ((charge / capacity) * 100).toInt()

val batteryIcon = when {
    percent <= 10 -> " "
    percent <= 35 -> ""
    percent <= 60 -> " "
    percent <= 85 -> ""
    else -> ""
}

val bolt = ""

val fullText = if (status == "Charging") "$bolt $batteryIcon $percent%" else "$batteryIcon $percent%"
val shortText = fullText
val color = when (status) {
    "Discharging" -> when {
        percent < 10 -> "#FF0000"
        percent < 35 -> "#FFAE00"
        percent < 60 -> "#FFF600"
        percent < 85 -> "#A8FF00"
        else -> "#00FF00"
    }
    else -> "00FF00"
}

println(fullText)
println(shortText)
if (percent < 5) {
    exitProcess(33)
}
println(color)
