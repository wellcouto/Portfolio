let popup = document.getElementById("popup");
let openBtn = document.getElementById("openBtn");
let closeBtn = document.getElementById("closeBtn");
let timePicker = document.getElementById("timePicker");

openBtn.onclick = function() {
    popup.style.display = "block";
}

closeBtn.onclick = function() {
    popup.style.display = "none";
}

window.onclick = function(event) {
    if (event.target === popup) {
        popup.style.display = "none";
    }
}

function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    if (sidebar.style.right === '0px' || sidebar.style.right === '') {
        sidebar.style.right = '-50%';
    } else {
        sidebar.style.right = '0px';
    }
}

// backbutton 

document.getElementById('backButton').addEventListener('click', function(e) {
    e.preventDefault();
    
    window.history.back();
});

// popup confirmation

function saveTime() {
    const dataInput = document.getElementById('timePicker');
    const horaEntradaInput = document.getElementById('horaEntrada');
    const horaSaidaInput = document.getElementById('horaSaida');
    const confirmationPopup = document.getElementById('confirmationPopup');
    const infoDaysContainer = document.getElementById('infoDaysContainer');

    if (horaEntradaInput.value && horaSaidaInput.value) {

        const dataAtual = new Date();
        const dia = dataAtual.getDate();
        const mes = dataAtual.getMonth() + 1; 
        const diaSemana = obterDiaSemana(dataAtual.getDay());


        const dataFormatada = `${dia.toString().padStart(2, '0')}/${mes.toString().padStart(2, '0')} - ${diaSemana}`;

        const newInfoDay = document.createElement('div');
        newInfoDay.classList.add('info-day');

        newInfoDay.innerHTML = `
            <p>${dataFormatada}</p>
            <p class="time" contenteditable="false">${horaEntradaInput.value}</p>
            <p class="digitalmente">Assinado Digitalmente</p>
            <p class="time" contenteditable="false">${horaSaidaInput.value}</p>
            <div class="edit-out-info">
                <button title="Editar" onclick="abrirPopupEdicao(this)">
                    <i class="bi bi-pencil-square"></i>
                </button>
                <button title="Deletar" onclick="abrirPopupDeletar()">
                    <i class="bi bi-trash3"></i>
                </button>
            </div>
        `;

        infoDaysContainer.appendChild(newInfoDay);

        confirmationPopup.style.display = 'flex';

        setTimeout(function() {
            confirmationPopup.style.display = 'none';
        }, 2000);

        dataInput.value = '';
        horaEntradaInput.value = '';
        horaSaidaInput.value = '';

        document.getElementById('saveButton').style.display = 'none';
    }
}

function obterDiaSemana(dia) {
    const diasSemana = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb'];
    return diasSemana[dia];
}

function verificarPreenchimento() {
    const dataInput = document.getElementById('timePicker');
    const horaEntradaInput = document.getElementById('horaEntrada');
    const horaSaidaInput = document.getElementById('horaSaida');
    const saveButton = document.getElementById('saveButton');

    if (dataInput.value && horaEntradaInput.value && horaSaidaInput.value) {
        saveButton.style.display = 'block'; 
    } else {
        saveButton.style.display = 'none'; 
    }
}

function preencherDataAtual() {
    const timePicker = document.getElementById('timePicker');
    
    const dataAtual = new Date();
    const ano = dataAtual.getFullYear();
    const mes = (dataAtual.getMonth() + 1).toString().padStart(2, '0');
    const dia = dataAtual.getDate().toString().padStart(2, '0');
    
    const dataFormatada = `${ano}-${mes}-${dia}`;
    
    timePicker.value = dataFormatada;
}

preencherDataAtual();

//// meses anteriores

function toggleMonths() {
    const months = document.getElementById('months');
    if (months.style.display === "none" || months.style.display === "") {
        months.style.display = "block";
    } else {
        months.style.display = "none";
    }
}

/// popup relatório
function mostrarPopupRelatorio() {
    const reportPopup = document.getElementById('reportPopupId');
    reportPopup.style.display = 'flex';
    
    setTimeout(function() {
      const reportGeradoPopup = document.getElementById('reportGeradoPopup');
      reportPopup.style.display = 'none'; 
      reportGeradoPopup.style.display = 'flex';
    }, 3000);
}
  
function fechaPopup() {
    const reportPopup = document.getElementById('reportPopupId');
    const reportGeradoPopup = document.getElementById('reportGeradoPopup');
    
    reportPopup.style.display = 'none';
    reportGeradoPopup.style.display = 'none';

}

////

function showCustomPopup() {
    const customPopup = document.getElementById('customPopupId');
    customPopup.style.display = 'block';
}

function closeCustomPopup() {
    const customPopup = document.getElementById('customPopupId');
    customPopup.style.display = 'none';
}

/// calendário 

function updateCalendar() {
    const currentDate = new Date();
    const months = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ];
    const daysOfWeek = [
        "Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"
    ];

    const currentMonth = months[currentDate.getMonth()];
    const currentDay = currentDate.getDate();
    const currentDayOfWeek = daysOfWeek[currentDate.getDay()];

    const currentMonthElement = document.getElementById('currentMonth');
    currentMonthElement.textContent = currentMonth;

    const currentDateElement = document.getElementById('currentDate');
    currentDateElement.textContent = currentDay;

    const currentDayOfWeekElement = document.getElementById('currentDayOfWeek');
    currentDayOfWeekElement.textContent = currentDayOfWeek;

    console.log('Atualização em tempo real:');
    console.log('Mês:', currentMonth);
    console.log('Dia:', currentDay);
    console.log('Dia da Semana:', currentDayOfWeek);
}

setInterval(updateCalendar, 1000);

updateCalendar();

//////

function obterHorarios() {
    const horarioEntrada = localStorage.getItem('horarioEntrada');
    const horarioSaida = localStorage.getItem('horarioSaida');

    if (horarioEntrada) {
        document.querySelectorAll('.time')[0].textContent = horarioEntrada;
    }

    if (horarioSaida) {
        document.querySelectorAll('.time')[1].textContent = horarioSaida;
    }
}

obterHorarios();

function verificarTeclaEnter(event) {
    if (event.key === 'Enter') {
        confirmarEdicao();
    }
}

function abrirPopupEdicao(botao) {
    const popupEdicao = document.getElementById('popupEdicao');
    popupEdicao.style.display = 'block';
}

function confirmarEdicao() {
    const horaEntradaInput = document.getElementById('novoHorarioEntrada');
    const horaSaidaInput = document.getElementById('novoHorarioSaida');


    if (infoDayParaEditar) {
        const timeElements = infoDayParaEditar.querySelectorAll('.time');
        if (timeElements.length >= 2) {
            timeElements[0].textContent = horaEntradaInput.value;
            timeElements[1].textContent = horaSaidaInput.value;
        }
    }

    fecharPopup('popupEdicao');
}

function abrirPopupDeletar() {
    const popupDeletar = document.getElementById('popupDeletar');
    popupDeletar.style.display = 'block';
}

function deletarInfoDay() {
    const infoDayContainer = document.getElementById('infoDaysContainer'); 
    const infoDays = infoDayContainer.getElementsByClassName('info-day'); 

    if (infoDays.length > 0) {

        infoDayContainer.removeChild(infoDays[infoDays.length - 1]);
    }

    fecharPopup('popupDeletar');
}

function fecharPopup(idPopup) {
    const popup = document.getElementById(idPopup);
    popup.style.display = 'none';
}


function fecharPopup(idPopup) {
    const popup1 = document.getElementById(idPopup);
    popup1.style.display = 'none';
}

document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') {

        fecharTodosPopups();
    }
});

function fecharTodosPopups() {
    const popups = document.querySelectorAll('.popup');


    popups.forEach(function (popup) {
        popup.style.display = 'none';
    });
}