const ls = localStorage;

// Calendar main
const Calendar = {

init() {
const today = new Date();
ScheduleManager.loadSchedule();

Calendar.showDates(today.getFullYear(), today.getMonth()+1);
    
Calendar.year = today.getFullYear();
Calendar.month = today.getMonth() + 1; //첫 달에서 두번째달 넘어가기(단, 달력데이터는 nan) -->134~


},

evtHandle(){
 document.querySelectorAll(".date")
  .forEach(elem => {
    elem.onclick = function () {
        //일정표 나오게 하기 start
        document.querySelector(".modal.schedule")
         .classList.add("show");

        const day  = Calendar.day = this.innerText; //일정표 날짜 나오기start
        const $mTitle = document.querySelector(".modal.schedule .modal-title");
        $mTitle.innerHTML = `Schedules <br> in ${Calendar.year}.${Calendar.month}. ${day}.`;
        
        Calendar.refreshScheduleList()
    }
});
},

refreshScheduleList(){
    const $mScheduleList = document.querySelector(".modal.schedule.schedule-list"); 
    const schedules = ScheduleManager.schedules
      .filter(v => v.date == `${Calendar.year}-${Calendar.month}-${Calendar.day}`);
  
      if (schedules.length)
        $mScheduleList.innerHTML = schedules.map(sc =>`
             <div class="schedule flex aic jcs">
             <h3>${sc.title}</h3>
             <button onclick="ScheduleManager.remove('${sc.id}')">x</button>
            </div>` 
        ).join("\n\n");
      else
        $mScheduleList.innerHTML = 
          `<div class="flex aic jcc" style="width: 100%; height:100px;">
            There is no Schedules... :(
          </div>`
          ;
},

showDates(y,m) {
    //일정표삭제 start
    const before = document.querySelectorAll(".date");
    before.forEach(v => v.remove());
   
    const today = new Date();
    //현재 날짜에 표시하기
    const todayDate = 
      y == today.getFullYear() &&
      m == today.getMonth() + 1
        ? today.getDate()
        : null ;
    console.log(todayDate);

   //첫째날 부터 마지막 날 까지 나오게 start
for (
    let i = -Calendar.getFirstDay(y, m) + 1;
    i < Calendar.getLastDate(y, m);
    i++
)   {
    const schedules = ScheduleManager.schedules
     .find( v=>v.date=='${y}-${m}-${i}');
     //스케줄이 있으면 표시.. start
    Calendar.$calendar.innerHTML += `
    <div class="date ${i < 1 ? "hidden-date" : ""} ${todayDate == i ? "today" : ""} ${schedules ? "has-schedule":""}"> 
     <p>${i}</p>
    </div>
    `;
}
    // 월이 넘어가도  일정표나오게 start
 Calendar.evtHandle(); 
},

//첫째날 부터 마지막 날 까지 나오게 start
getFirstDay(y, m) {
const date = new Date(`${y}-${m}-01`);
return date.getDay();
},
getLastDate(y, m) {
const date = new Date(y, m, 0);
return date.getDate();
},

//월 넘어갈때 데이터 받아서 정상정인 달력으로 출력하기
addMonth(m){
    const date = new Date(
        Calendar.year, Calendar.month + m -1, 1
    );
    Calendar.year = date.getFullYear();
    Calendar.month = date.getMonth() + 1 ;

    Calendar.showDates(Calendar.year, Calendar.month );
    Calendar.$date.innerHTML = `${Calendar.year}. ${Calendar.month}`
}

};

const ScheduleManager = {
    
    schedules: [],

loadSchedule() {
  if(!ls['schedules']) return;


  ScheduleManager.Schedules = 
    JSON.parse(ls['schedules']);   
},

saveSchedule(){
    ls['schedules'] =
        JSON.stringify(ScheduleManager.schedules);
},

//일정추가하기
addSchedule() {
  const title = prompt("what is title of schedule?");

  if (!title.match(/^[a-zA-Z0-9ㄱ-힣 !]*$/g)) //영문 대,소문자 찾기.0~9숫자찾기.한글찾기(g=모두)
    return alert("Incorrect title.");

  const id = new Date().getTime();
  this.schedules.push({
        id,
        date: `${Calendar.year}-${Calendar.month}-${Calendar.day}`,
        title
      });

      this.saveSchedule();
      Calendar.refreshScheduleList();
      Calendar.showDates(Calendar.year, Calendar.month);
},

remove(id) {
    const  index = ScheduleManager.schedules
    .findIndex(v => v.id == id);

        ScheduleManager.schedules
        .splice(index,1);

        this.saveSchedule();
        Calendar.refreshScheduleList();
        Calendar.showDates(Calendar.year, Calendar.month);
}
}