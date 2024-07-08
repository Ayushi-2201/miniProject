let boxes = document.querySelectorAll(".box");

let resetBtn = document.querySelector(".reset");

let winnerDeclaration = document.querySelector(".winnerDeclaration");

let turn = true;

let winningPatterns = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
];

boxes.forEach((ele) => {
    ele.addEventListener("click", () => {
        if (turn) {
            ele.innerHTML = "X";
        } else {
            ele.innerHTML = "O";
        }
        turn = !turn;
        ele.disabled = true;

        checkWinner();
    });
});

const checkWinner = () => {
    let winnerFound = false;

    for (let pattern of winningPatterns) {
        let pos1Val = boxes[pattern[0]].innerHTML;
        let pos2Val = boxes[pattern[1]].innerHTML;
        let pos3Val = boxes[pattern[2]].innerHTML;

        if (pos1Val !== "" && pos2Val !== "" && pos3Val !== "") {
            if (pos1Val === pos2Val && pos2Val === pos3Val) {
                if (!turn) {
                    winnerDeclaration.innerHTML = "Winner is: Player X";
                } else {
                    winnerDeclaration.innerHTML = "Winner is: Player O";
                }

                boxes.forEach((ele) => {
                    ele.disabled = true;
                });
                winnerDeclaration.style.display = "block";
                winnerFound = true;
                break;
            }
        }
    }

    // Check for a tie if no winner is found
    if (!winnerFound) {
        let allBoxesFilled = true;
        boxes.forEach((ele) => {
            if (ele.innerHTML === "") {
                allBoxesFilled = false;
            }
        });

        if (allBoxesFilled) {
            winnerDeclaration.innerHTML = "It's a tie!";
            winnerDeclaration.style.display = "block";
        }
    }
};

resetBtn.onclick = () => {
    boxes.forEach((ele) => {
        ele.innerHTML = "";
        ele.disabled = false;
    });
    winnerDeclaration.style.display = "none";
    winnerDeclaration.innerHTML = "Winner is :";
    turn = true; // Reset the turn to the initial state
};
