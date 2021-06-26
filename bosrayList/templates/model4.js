[ng\:cloak], [ng-cloak], .ng-cloak {
    display: none;
}

* {
	box-sizing: border-box;
}

html,body {
	margin: 0;
	background: #222;
}

.app-container {
	border-radius: 4px;
	overflow: hidden;
	width: 720px;
	height: auto;
	max-width: 100%;
	position: absolute;
	top: 120px;
	left: 0;
	right: 0;
	margin: auto;
}
.buttons-container {
	position: absolute;
	bottom: 15px;
	right: 0;
	height: 40px;
	font-family: "Roboto", sans-serif;
}
.cancel-button,
.save-button {
	float: left;
	height: 40px;
	line-height: 40px;
	padding: 0 15px;
	border-radius: 2px;
	margin-right: 15px;
	cursor: pointer;
	transition: all 0.15s ease;
}
.cancel-button {
	background: white;
	color: #0DAD83;
}
.save-button {
	background: #0DAD83;
	color: white;
}

/* Datepicker Stuff */
.datepicker {
    position: relative;
	width: 100%;
    display: block;
    -webkit-tap-highlight-color: rgba(0,0,0,0);
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    -o-user-select: none;
    user-select: none;
    font-family: "Roboto", sans-serif;
	overflow: hidden;
	transition: background 0.15s ease;
}
.datepicker.am {
	background: white;
}
.datepicker.pm {
	background: #0DAD83;
}
.datepicker-header {
	width: 100%;
    color: white;
	overflow: hidden;
}
.datepicker-title {
	width: 50%;
	float: left;
	height: 60px;
	line-height: 60px;
	padding: 0 15px;
	text-align: left;
	font-size: 20px;
}
.datepicker-subheader {
	width: 50%;
	float: left;
	height: 60px;
	line-height: 60px;
	font-size: 14px;
	padding: 0 15px;
	text-align: right;
}
.datepicker-calendar {
    // background: white;
    width: 50%;
	float: left;
    padding: 20px 15px 15px;
    max-width: 400px;
    display: block;
}
.calendar-header {
    color: black;
    font-weight: bolder;
    text-align: center;
    font-size: 18px;
    padding: 10px 0;
    position: relative;
}
.current-month-container {
    display: inline-block;
    height: 30px;
    position: relative;
}
.goback,
.goforward {
    height: 30px;
    width: 30px;
    border-radius: 30px;
    display: inline-block;
    cursor: pointer;
    position: relative;
    top: -4px;
}
.goback path,
.goforward path {
	transition: stroke 0.15s ease;
}
.goback {
    float: left;
    margin-left: 3.8%;
}
.goforward {
    float: right;
    margin-right: 3.8%;
}
.calendar-day-header {
    width: 100%;
    position: relative;
}
.day-label {
    color: #8A8A8A;
    padding: 5px 0;
    width: 14.2857142%;
    display: inline-block;
    text-align: center;
}
.datecontainer {
    width: 14.2857142%;
    display: inline-block;
    text-align: center;
    padding: 4px 0;
}
.datenumber {
    max-width: 35px;
    max-height: 35px;
    line-height: 35px;
    margin: 0 auto;
    color: #8A8A8A;
    position: relative;
    text-align: center;
    cursor: pointer;
    z-index: 1;
    transition: all .25s cubic-bezier(0.7,-0.12, 0.2, 1.12);
}
.no-hover .datenumber,
.no-hover .datenumber:hover,
.no-hover .datenumber:before,
.no-hover .datenumber:hover::before {
    cursor: default;
    color: #8A8A8A;
    background: transparent;
    opacity: 0.5;
}
.no-hover .datenumber.day-selected {
    color: white;
}
.datenumber:hover {
    color: white;
}
.datenumber:before {
    content: '';
    display: block;
    position: absolute;
    height: 35px;
    width: 35px;
    border-radius: 100px;
    z-index: -1;
    background: transparent;
    -webkit-transform: scale(0.75);
    -moz-transform: scale(0.75);
    -ms-transform: scale(0.75);
    -o-transform: scale(0.75);
    transform: scale(0.75);
    transition: all .25s cubic-bezier(0.7,-0.12, 0.2, 1.12);
    transition-property: background, transform, color, border;
}
.datenumber:hover::before {
    background: #FFAB91;
    -webkit-transform: scale(1);
    -moz-transform: scale(1);
    -ms-transform: scale(1);
    -o-transform: scale(1);
    transform: scale(1);
}
.day-selected {
    color: white;
}
.datenumber.day-selected:before {
    background: #FF6E40;
    -webkit-transform: scale(1);
    -moz-transform: scale(1);
    -ms-transform: scale(1);
    -o-transform: scale(1);
    transform: scale(1);
    -webkit-animation: select-date .25s forwards;
    -moz-animation: select-date .25s forwards;
    animation: select-date .25s forwards;
}
@-webkit-keyframes select-date {
    0% { background: #FFAB91; }
    100% { background: #FF6E40; }
}
@keyframes select-date {
    0% { background: #FFAB91; }
    100% { background: #FF6E40; }
}

/* timepicker styles */
.timepicker-container-outer {
  width: 50%;
  max-width: 700px;
  float: left;
  display: block;
  padding: 40px 30px 30px;
  position: relative;
  top: 50px;
  overflow: hidden;
  -webkit-tap-highlight-color: transparent;
  transition: background 0.15s ease;
}

.timepicker-container-inner {
  width: 100%;
  height: 100%;
  max-width: 320px;
  margin: 0 auto;
  position: relative;
  display: block;
}

.timeline-container {
  display: block;
  float: left;
  position: relative;
  width: 100%;
  height: 36px;
}

.current-time {
  display: block;
  position: absolute;
  z-index: 1;
  width: 40px;
  height: 40px;
  border-radius: 20px;
  top: -25px;
  left: -20px;
  cursor: pointer;
  -webkit-user-select: none;
     -moz-user-select: none;
      -ms-user-select: none;
          user-select: none;
}
.current-time::after {
  content: '';
  display: block;
  width: 40px;
  height: 40px;
  position: absolute;
  background: #FF6E40;
  transition: all 0.15s ease; 
  -webkit-transform: rotate(45deg);
          transform: rotate(45deg);
  border-radius: 20px 20px 3px 20px;
  z-index: -1;
  top: 0;
}

.actual-time {
  color: white;
  line-height: 40px;
  font-size: 12px;
  text-align: center;
  transition: all 0.15s ease;
}

.timeline {
  display: block;
  z-index: 1;
  width: 100%;
  height: 2px;
  position: absolute;
  bottom: 0;
}
.timeline::before, .timeline::after {
  content: '';
  display: block;
  width: 2px;
  height: 10px;
  top: -6px;
  position: absolute;
  background: #0DAD83;
  left: -1px;
  transition: background 0.15s ease;
}
.timeline::after {
  left: auto;
  right: -1px;
}

.hours-container {
  display: block;
  z-index: 0;
  width: 100%;
  height: 10px;
  position: absolute;
  top: 31px;
  left: 1px;
}

.hour-mark {
  width: 2px;
  display: block;
  float: left;
  height: 4px;
  background: #0DAD83;
  position: relative;
  margin-left: calc((100% / 12) - 2px);
  transition: background 0.15s ease;
}
.hour-mark:nth-child(3n) {
  height: 6px;
  top: -1px;
}

.display-time {
  width: calc(60% - 30px);
  display: block;
  margin-top: 30px;
  height: 36px;
  line-height: 36px;
  overflow: hidden;
  float: left;
  position: relative;
  font-size: 20px;
  text-align: center;
  transition: color 0.15s ease;
}
.decrement-time,
.increment-time {
  cursor: pointer;
  position: absolute;
  display: block;
  width: 24px;
  height: 24px;
  line-height: 24px;
  top: 6px;
  font-size: 20px;
}
.decrement-time {
  left: 0;
  text-align: left;
}
.increment-time {
  right: 0;
  text-align: right;
}
.increment-time path,
.decrement-time path{
	transition: all 0.15s ease;
}
.time {
    width: calc(100% - 48px);
	position: relative;
	left: 24px;
	height: 36px;
	&:after {
		content: '';
		height: 2px;
		width: 100%;
		position: absolute;
		bottom: 0;
		background: white;
		left: 0;
		right: 0;
		opacity: 0.5;
		transition: all 0.15s ease;
	}
}
.time.time-active:after {
	display: none;
}
.time-input {
	position: absolute;
	top: 0;
	left: 0;
	right: 0;
	height: 34px;
	line-height: 34px;
	bottom: 2px;
	width: 100%;
	border: none;
	background: none;
	text-align: center;
	color: white;
	font-size: inherit;
	opacity: 0;
	transition: all 0.15s ease;
	cursor: pointer;
	&:focus,
	&:active {
		outline: none;
	}
}
.formatted-time {
	cursor: pointer;
}
.time-input:focus {
	cursor: auto;
	& ~ .formatted-time {
		border-radius: 2px;
		background: #0DAD83;
		color: white;
		cursor: default;
	}
}

.am-pm-container {
  width: 40%;
  padding-left: 15px;
  float: right;
  height: 36px;
  line-height: 36px;
  display: block;
  position: relative;
  margin-top: 30px;
}

.am-pm-button {
  width: calc(50% - 5px);
  height: 36px;
  line-height: 36px;
  background: #2196F3;
  text-align: center;
  color: white;
  border-radius: 4px;
  float: left;
  cursor: pointer;
}
.am-pm-button:first-child {
  background: #0DAD83;
  color: white;
}
.am-pm-button:last-child {
  background: white;
  color: #0DAD83;
  margin-left: 10px;
}

@-webkit-keyframes select-date-pm {
	0% { background: rgba(255,255,255,0.5); }
	100% { background: #FFF; }
}
@keyframes select-date-pm {
	0% { background: rgba(255,255,255,0.5); }
	100% { background: #FFF; }
}


.datepicker.am {
	.datepicker-header {
		color: white;
		background: #0DAD83;
	}
	.current-time::after {
		background: #0DAD83;
	}
	.actual-time {
	    color: white;
	}
	.display-time {
	    color: #FF6E40;
	}
	.time-input {
		color: #FF693C;
	}
	.time:after {
		background: #FF693C;
	}
	.increment-time path,
	.decrement-time path{
		stroke: #FF693C;
	}
}

.datepicker.pm {
	.datepicker-header {
		background: white;
		color: #FF693C;
	}
	.datepicker-subheader {
		color: #0DAD83;
	}
	
	.goback:before,
	.goback:after,
	.goforward:before,
	.goforward:after {
		background: white;
	}
	.day-label {
		color: white;
	}
	.datenumber {
		color: white;
	}
	.datenumber:hover::before {
		background: rgba(255,255,255,0.5);
		-webkit-transform: scale(1);
		-moz-transform: scale(1);
		-ms-transform: scale(1);
		-o-transform: scale(1);
		transform: scale(1);
	}
	.datenumber.day-selected {
		color: #FF693C;
	}
	.datenumber.day-selected:before {
		background: white;
		-webkit-animation: select-date-pm .25s forwards;
		-moz-animation: select-date-pm .25s forwards;
		animation: select-date-pm .25s forwards;
	}
	.current-month-container {
		color: white;
	}
	.current-time::after {
	    background: white;
	}
	.actual-time {
	    color: #FF6E40;
	}
	.display-time {
    	color: white;
	}
	.timeline::before, .pm .timeline::after {
	    background: white;
	}
	.hour-mark {
		background: white;
	}
	.am-pm-button:last-child {
		color: #FF6E40;
	}
	.cancel-button {
		background: none;
		color: white;
	}
	.save-button {
		background: white;
		color: #FF693C;
	}
	.goback path,
	.goforward path {
		stroke: white;
	}
	.time-input:focus ~ .formatted-time {
		background: white;
		color: #FF693C;
	}
}

.datepicker.compact {
	.datepicker-title,
	.datepicker-subheader {
		width: 100%;
		text-align: center;
	}
	.datepicker-title {
		height: 50px;
		line-height: 50px;
	}
	.datepicker-subheader {
		height: 30px;
		line-height: 30px;
	}
    .display-time {
        width: 60%;
        font-size: 20px;
        line-height: 36px;
    }
	.app-container {
		width: 100%;
	}
	.datepicker-calendar {
		width: 100%;
		margin: 0 auto;
		float: none;
	}
	.timepicker-container-outer {
		width: 100%;
		margin: 0 auto;
		float: none;
		top: -15px;
	}
	.buttons-container {
		position: relative;
		float: right;
	}
}

