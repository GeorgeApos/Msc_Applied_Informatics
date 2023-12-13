let team1Score = 0;
let team2Score = 0;
let team1Sets = 0;
let team2Sets = 0;
let winningPoints1 = 0;
let winningPoints2 = 0;
let servingTeam = null;
let isTimeoutRunning = false;

function increaseScore(team) {
    if (team === 1) {
        team1Score++;
        winningPoints1++;
        document.getElementById('team1Score').innerText = team1Score;
        if (team1Score === 8 || team1Score === 16) {
            startTimer();
        }
        servingTeam = 1;
        highlightServingTeam();
    } else {
        team2Score++;
        winningPoints2++;
        document.getElementById('team2Score').innerText = team2Score;
        if (team2Score === 8 || team2Score === 16) {
            startTimer();
        }
        servingTeam = 2;
        highlightServingTeam();
    }

    checkScores();
}

function highlightServingTeam() {
    const servingTeamP = document.getElementById('servingTeamParagraph');
    const team1 = document.getElementById('team1Name');
    const team2 = document.getElementById('team2Name');

    if (servingTeam === 1) {
        servingTeamP.innerText = team1.value;
        servingTeamP.style.fontWeight = 'bold';
        team1.style.fontWeight = 'bold'; 
        team2.style.fontWeight = 'normal'; 
    } else if (servingTeam === 2) {
        servingTeamP.innerText = team2.value;
        servingTeamP.style.fontWeight = 'bold';
        team1.style.fontWeight = 'normal';
        team2.style.fontWeight = 'bold';
    } else {
        servingTeamP.innerText = 'None';
        servingTeamP.style.fontWeight = 'normal';
        team1.style.fontWeight = 'normal';
        team2.style.fontWeight = 'normal';
    }
}

function changeService() {
    highlightServingTeam();
}

function checkScores() {
    const MIN_SET_SCORE = 25;
    const MIN_FIFTH_SET_SCORE = 15;
    const SETS_TO_WIN = 3;
    const TIEBREAK_SET = 5;

    const winnerInfoElement = document.getElementById('winnerInfo');

    if (team1Score >= MIN_SET_SCORE && team1Score - team2Score >= 2) {
        team1Sets++;
        resetScores();
    } else  if (team2Score >= MIN_SET_SCORE && team2Score - team1Score >= 2) {
        team2Sets++;
        resetScores();
    }

    updateSetsInfo();

    if (team1Sets === SETS_TO_WIN) {
        winnerInfoElement.innerText = "Team 1 wins!";
    } else if (team2Sets === SETS_TO_WIN) {
        winnerInfoElement.innerText = "Team 2 wins!";
    }

    if (team1Sets === TIEBREAK_SET && team2Sets === TIEBREAK_SET) {
        if (team1Score >= MIN_FIFTH_SET_SCORE && team1Score - team2Score >= 2) {
            winnerInfoElement.innerText = "Team 1 wins!";
        } else if (team2Score >= MIN_FIFTH_SET_SCORE && team2Score - team1Score >= 2) {
            winnerInfoElement.innerText = "Team 2 wins!";
        }
    }
}

function updateSetsInfo() {
    const setsInfoElement = document.getElementById('setsInfo');
    setsInfoElement.innerText = `${team1Sets} - ${team2Sets}`;
}

function resetScores() {
    team1Score = 0;
    team2Score = 0;
    document.getElementById('team1Score').innerText = team1Score;
    document.getElementById('team2Score').innerText = team2Score;
    isTimeoutRunning = false;
    clearInterval(countdown);
}

function startTimer() {
    if (!isTimeoutRunning) {
        let timeLeft = 60; 
        const timerElement = document.getElementById('timer');
        isTimeoutRunning = true;

        const countdown = setInterval(() => {
            if (timeLeft <= 0) {
                clearInterval(countdown);
                timerElement.innerText = 'Timeout!';
                isTimeoutRunning = false;
            } else {
                timerElement.innerText = timeLeft + 's';
                timeLeft--;
            }
        }, 1000);
    }
}

function exportScore() {
    const team1Name = document.getElementById('team1Name').value;
    const team2Name = document.getElementById('team2Name').value;

    const data = [
        ['HomeTeam', 'AwayTeam', 'HomeSets', 'AwaySets', 'HomePoints', 'AwayPoints'],
        [team1Name, team2Name, team1Sets, team2Sets, winningPoints1, winningPoints2]
    ];

    const csvContent = 'data:text/csv;charset=utf-8,' + data.map(row => row.join(',')).join('\n');
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement('a');
    link.setAttribute('href', encodedUri);
    link.setAttribute('download', 'volleyball_match.csv');
    document.body.appendChild(link);
    link.click();
}