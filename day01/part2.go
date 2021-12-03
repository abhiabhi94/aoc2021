package main

import (
	"bufio"
	"fmt"
	"os"
    "path/filepath"
    "strconv"
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


func getInputs() []int {
    file := getInputFile()
    scanner := bufio.NewScanner(file)

	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "reading standard input:", err)
	}

    var records []int
    for scanner.Scan() {
        records = append(records, toInt(scanner.Text()))
    }
    return records
}


func toInt(value string) int {
    num, err := strconv.Atoi(value)
    handleError(err)
    return num
}


func Calculate() int {

    depths := getInputs()
    length := len(depths)
    increased := 0
    for index := 0; index < length - 3; index++ {
        previousDepth := depths[index]
        nextDepth := depths[index + 3]
        if nextDepth > previousDepth {
            increased += 1
        }
    }
    return increased
}


func main() {
    fmt.Println(Calculate())
}
