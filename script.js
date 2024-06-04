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


  const inputText = document.querySelector('.input-text');
  const sortBtn = document.querySelector('.sort-btn');
  const chute1 = document.querySelector('.chute1');
  const chute2 = document.querySelector('.chute2');
  const chute3 = document.querySelector('.chute3');
  const messages = document.querySelector('.messages');
  
  let chute1Count = 0;
  let chute2Count = 0;
  let chute3Count = 0;
  
  function sortItems() {
    const input = inputText.value.toLowerCase();
    inputText.value = '';
  
    if (input === '1') {
      if (chute3Count < 3) {
        const item = document.createElement('div');
        item.classList.add('item', 'item1');
        chute3.appendChild(item);
        chute3Count++;
        setTimeout(() => {
          item.remove();
        }, 3000);
      } else {
        messages.textContent = 'Chute 3 is full';
      }
    } else if (input === '2') {
      if (chute2Count < 3) {
        const item = document.createElement('div');
        item.classList.add('item', 'item2');
        chute2.appendChild(item);
        chute2Count++;
        setTimeout(() => {
          item.remove();
        }, 3000);
      } else {
        messages.textContent = 'Chute 2 is full';
      }
    } else if (input === '3') {
      if (chute1Count < 3) {
        const item = document.createElement('div');
        item.classList.add('item', 'item3');
        chute1.appendChild(item);
        chute1Count++;
        setTimeout(() => {
          item.remove();
        }, 3000);
      } else {
        messages.textContent = 'Chute 1 is full';
      }
    }
  }
  
  sortBtn.addEventListener('click', sortItems);