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

  document.getElementById('animationForm').addEventListener('submit', function(e) {
    e.preventDefault();  // 阻止表单默认提交行为
    var animationCase = document.getElementById('animationCase').value;

    fetch('/process_case', {
        method: 'POST',
        body: new URLSearchParams({'animationCase': animationCase}),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
    .then(response => response.json())
    .then(data => {
        alert(data.result);  // 使用 alert 或其他方式在页面上显示结果
        startAnimation(animationCase);  // 根据服务器响应触发动画
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

function startAnimation(caseType) {
    const conveyor = document.getElementById('conveyor');
    conveyor.innerHTML = ''; // 清空传送带上的内容
    const workpiece = document.createElement('div');
    workpiece.classList.add('workpiece');
    workpiece.style.position = 'absolute'; // 确保工件可以移动

    if (caseType === 'case1') {
        workpiece.style.backgroundColor = 'black';
    } else if (caseType === 'case2') {
        workpiece.style.backgroundColor = 'silver';
    } else if (caseType === 'case3') {
        workpiece.style.backgroundColor = 'red';
    } else {
        alert('Invalid case');
        return;
    }

    conveyor.appendChild(workpiece);
    let position = 0;
    const interval = setInterval(() => {
        position += 5;
        workpiece.style.left = position + 'px';

        if (position >= 580) {
            clearInterval(interval);
            conveyor.removeChild(workpiece);
        } else if (caseType === 'case1' && position >= 500) {
            clearInterval(interval);
            workpiece.style.top = '40px';
            workpiece.style.left = '500px';
            setTimeout(() => conveyor.removeChild(workiece), 500);
        } else if (caseType === 'case2' && position >= 300) {
            clearInterval(interval);
            workpiece.style.top = '40px';
            workpiece.style.left = '300px';
            setTimeout(() => conveyor.removeChild(workpiece), 500);
        } else if (caseType === 'case3' && position >= 100) {
            clearInterval(interval);
            workpiece.style.top = '40px';
            workpiece.style.left = '100px';
            setTimeout(() => conveyor.removeChild(workpiece), 500);
        }
    }, 100); // 调整时间间隔以控制动画速度
}