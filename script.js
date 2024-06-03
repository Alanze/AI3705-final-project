document.getElementById('myForm').addEventListener('submit', function(event) {
    event.preventDefault();
  
    setTimeout(function() {
      document.getElementById('message').innerHTML = `
        <blockquote>
          Assistant: Based on the requirement document, I will extract the information into structured text using the defined module types: <strong>Object</strong>, <strong>Status</strong>, <strong>Module</strong>, and <strong>Action</strong>.
        </blockquote>
      `;
    }, 1000);
  
    setTimeout(function() {
      document.getElementById('message').innerHTML += `
        <h3>Objects:</h3>
        <ol>
          <li>Workpiece</li>
          <li>Conveyor belt</li>
          <li>Barrier arm</li>
          <li>Sorting arm 1</li>
          <li>Sorting arm 2</li>
          <li>Chute 1</li>
          <li>Chute 2</li>
          <li>Chute 3</li>
        </ol>
      `;
    }, 2000);
  
    setTimeout(function() {
      document.getElementById('message').innerHTML += `
        <h3>Statuses:</h3>
        <ol>
          <li>atFront (Workpiece is at the front of the conveyor belt)</li>
          <li>stopped (Conveyor belt is stopped)</li>
          <li>extended (Barrier arm is extended)</li>
          <li>retracted (Barrier arm is retracted)</li>
          <li>full (Chute is full)</li>
          <li>notFull (Chute is not full)</li>
        </ol>
      `;
    }, 3000);
  
    setTimeout(function() {
      document.getElementById('message').innerHTML += `
        <h3>Modules:</h3>
        <ol>
          <li>Color detection module</li>
          <li>Electromagnetic sorting arms</li>
          <li>Retroreflective photoelectric sensor</li>
        </ol>
      `;
    }, 4000);

    setTimeout(function() {
      document.getElementById('message').innerHTML += `
        <h3>Actions:</h3>
        <ol>
          <li>Detect (Color detection module detects the material and color of the workpiece)</li>
          <li>Stop (Conveyor belt stops)</li>
          <li>Extend (Barrier arm extends)</li>
          <li>Retract (Barrier arm retracts)</li>
          <li>Sort (Sorting arm sorts the workpiece into a chute)</li>
          <li>Start (Conveyor belt starts moving)</li>
          <li>Store (Workpiece is stored in a chute)</li>
        </ol>
      `;
    }, 5000);

    setTimeout(function() {
      document.getElementById('message').innerHTML += `
        <h3>Structured Text:</h3>
        <ol>
          <li>Workpiece Object, atFront Status, conveyorBelt Object</li>
          <li>conveyorBelt Object, stopped Status</li>
          <li>barrierArm Module, extended Status</li>
          <li>sortingArm1 Module, retracted Status</li>
          <li>sortingArm2 Module, retracted Status</li>
          <li>chute1 Object, notFull Status</li>
          <li>chute2 Object, notFull Status</li>
          <li>chute3 Object, notFull Status</li>
          <li>colorDetectionModule Module, Detect Action</li>
          <li>electromagneticSortingArms Module, Sort</li>
        </ol>
      `;
    }, 6000);
  });


const conveyorBelt = document.querySelector('.conveyor-belt');
const slots = document.querySelectorAll('.slot');
const startBtn = document.getElementById('start-btn');
const resetBtn = document.getElementById('reset-btn');

let items = [];
let isRunning = false;

function createItem() {
  const item = document.createElement('div');
  item.classList.add('item');
  item.style.backgroundColor = getRandomColor();
  conveyorBelt.appendChild(item);
  items.push(item);
}

function getRandomColor() {
  const colors = ['black', 'red', 'gold'];
  return colors[Math.floor(Math.random() * colors.length)];
}

function moveItems() {
  items.forEach(item => {
    item.style.left = `${parseFloat(item.style.left) + 1}px`;
    if (parseFloat(item.style.left) >= conveyorBelt.offsetWidth) {
      item.style.left = '0';
      sortItem(item);
    }
  });
  if (isRunning) {
    requestAnimationFrame(moveItems);
  }
}

function sortItem(item) {
  const color = item.style.backgroundColor;
  if (color === 'black') {
    slots[2].appendChild(item);
  } else if (color === 'red') {
    slots[0].appendChild(item);
  } else {
    slots[1].appendChild(item);
  }
  checkSlotFull();
}

function checkSlotFull() {
  for (let i = 0; i < slots.length; i++) {
    if (slots[i].children.length === 3) {
      stopSystem();
    }
  }
}

function stopSystem() {
  isRunning = false;
  alert('One of the slots is full. The system has stopped.');
}

startBtn.addEventListener('click', () => {
  if (!isRunning) {
    isRunning = true;
    createItem();
    moveItems();
  }
});

resetBtn.addEventListener('click', () => {
  isRunning = false;
  items.forEach(item => item.remove());
  items = [];
  for (let i = 0; i < slots.length; i++) {
    slots[i].innerHTML = '';
  }
});