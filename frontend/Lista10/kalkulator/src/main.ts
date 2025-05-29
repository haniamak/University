
const display = document.getElementById("display") as HTMLInputElement | null;

function appendToDisplay(input: string): void {
  if (display) {
    display.value += input;
  }
}

function clearDisplay(): void {
  if (display) {
    display.value = "";
  }
}

function calculate(): void {
  if (display) {
    try {
      // Use Function constructor for safer evaluation than eval (still not fully safe)
      // eslint-disable-next-line no-new-func
      display.value = Function(`"use strict";return (${display.value})`)().toString();
    } catch (error) {
      display.value = "Error";
    }
  }
}

(window as any).appendToDisplay = appendToDisplay;
(window as any).clearDisplay = clearDisplay;
(window as any).calculate = calculate;
