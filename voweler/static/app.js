
var SCORE_SEP = ' / ';

function shuffle(array) {
    let counter = array.length;

    // While there are elements in the array
    while (counter > 0) {
        // Pick a random index
        let index = Math.floor(Math.random() * counter);

        // Decrease counter by 1
        counter--;

        // And swap the last element with it
        let temp = array[counter];
        array[counter] = array[index];
        array[index] = temp;
    }

    return array;
}

function updateVowels (vowels) {
    $('.letter').each(function(ix, val){
        if (vowels.indexOf(val.innerHTML) > -1) {
            $(val).addClass('vowel')
        } else {
            $(val).removeClass('vowel')
        }

    })
}


function getLetters () {
    var rv = [];
    $('.letter').each(function(ix, val){
        rv.push(val.innerHTML)
    })
    return rv
}


function isVowel(c) {
    return ['a', 'e', 'i', 'o', 'u', 'y'].indexOf(c) !== -1
}


function getVowels() {
    return getLetters().filter(isVowel) 
}


function getConsonants() {
    return getLetters().filter(function(c) {
        return !isVowel(c)
    })  
}


function updateWeights (weights) {  
    var head = ["Weights"];
    var data = {columns: [head.concat(weights)]};
    chart.load(data);
}

function trainLetters(letters) {
    var interval = 50;
    shuffle(letters);
    letters
        .forEach(function(letter, index) {
            setTimeout(
                getState.bind(undefined, letter),
                interval * index )
        });
}

function trainAlphabet() {
    trainLetters(getLetters());
}

function trainVowels() {
    trainLetters(getVowels());
}

function trainConsonants() {
    trainLetters(getConsonants());
}


function getState(letter) {
    var url = '/state';
    var data;
    if (letter) {
        data = {update: letter}
    }

    $.ajax({
        url: url,
        type: 'get',
        data: data,
        success: function(data) {
            updateVowels(data.vowels);
            updateWeights(data.weights);
            updatePlot(data.scatter_data, plot);
            updateScore(data.current_score, 0);
        },
        error: function(err) {
            console.log(err)
        }
    })
}

function updatePlot (separation_data, c3_plot) {
    var load_data = {
        xs: {
            consonant: 'consonant_x',
            vowel: 'vowel_x',
        },
        columns: separation_data
    };

    c3_plot.load(load_data);
}

function updateScore(value, index) {
    var current_scores = $('#score').text().split(SCORE_SEP);
    current_scores[index] = value;
    $('#score').text(current_scores.join(SCORE_SEP));
}

function setSize() {
    // sets new vector size for character embedding
    // updates page with new perceptron state
    var size = $('#size')[0].value;
    var data = {"size": size};
    $.ajax({
        url: '/size',
        type: 'get',
        data: data,
        success: function(data) {
            updateScore(data.score, 1);
            updatePlot(data.scatter_data, lda_plot);
        },
        error: function(err) {
            console.log(err)
        }       
    });
    getState();
}

function initializeScatter(bind) {
    return c3.generate({
        bindto: bind,
        size: {
            height: 100,
        },
        data: {
            xs: {
                consonant: 'consonant_x',
                vowel: 'vowel_x',
            },
            type: 'scatter',
            columns: []
        },
        axis: {
            x: {
                tick: {
                    fit: false
                },
                min: -2.5,
                max: 2.5
            },
            y: {
                max: 1.2,
                min: .9,
                padding: {
                  top: 100,
                  bottom: 100
                },
                show: false
            }
        },
        point: {
            r: 15
        }
    })
}


var chart = c3.generate({
    bindto: '#chart',
    data: {
        columns: [],
        type: 'bar'
    },
    bar: {
        width: {
            ratio: .5 
        }
    },
    axis: {
        y: {
            tick: {
                format: function (d) {return d.toString().substr(0, 4)}
            }
        }
    }
});

var plot = initializeScatter('#plot');
var lda_plot = initializeScatter('#lda_plot');

getState();
setSize();
