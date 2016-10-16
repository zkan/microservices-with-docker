package main

import (
	"encoding/json"
	"net/http"
)

type Data struct {
	Celsius float32 `json:"celsius"`
}

func main() {
	http.HandleFunc("/", getCelsius)
	http.ListenAndServe(":3000", nil)
}

func getCelsius(w http.ResponseWriter, r *http.Request) {
	data := Data{25.6}

	js, err := json.Marshal(data)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.Write(js)
}
