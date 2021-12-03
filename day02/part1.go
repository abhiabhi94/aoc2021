package main

import (
	"bufio"
	"fmt"
	"os"
    "path/filepath"
    "strconv"
    "strings"
)

func handleError(err error) {
    if err != nil {
        panic(err)
    }
}

func getInputFile() *os.File {
    currentFilePath, err := os.Executable()
    handleError(err)
    baseDir := filepath.Dir(currentFilePath)
    file, err := os.Open(filepath.Join(baseDir, "input.txt"))
    handleError(err)

    return file
}


func getInputs() ([]string, []int) {
    file := getInputFile()
    scanner := bufio.NewScanner(file)

	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "reading standard input:", err)
	}

    var directions []string
    var units []int
    for scanner.Scan() {
        instruction := scanner.Text()
        direction_and_unit := strings.Split(instruction, " ")
        direction := direction_and_unit[0]
        unit := direction_and_unit[1]
        directions = append(directions, direction)
        units = append(units, toInt(unit))
    }
    return directions, units
}


func toInt(value string) int {
    num, err := strconv.Atoi(value)
    handleError(err)
    return num
}


func Calculate() int {

    directions, units := getInputs()
    length := len(directions)
    abscissa := 0
    ordinate := 0
    for index := 0; index < length; index++ {
        direction := strings.ToLower(directions[index])
        unit := units[index]
        if direction == "forward"{
            abscissa += unit
        } else if direction == "down"{
            ordinate += unit
        } else if direction == "up"{
            ordinate -= unit
        }
    }
    return abscissa * ordinate
}


func main() {
    fmt.Println(Calculate())
}
