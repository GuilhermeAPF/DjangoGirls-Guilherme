$(document).ready(function(){

	tododatabase = {
		load_todos_from_localstorage() {
			var strtodos = localStorage.getItem('todos')
			if (strtodos === null) {
				localStorage.setItem('todos', "[]")
				return []
			} else {
				return JSON.parse(strtodos)
			}
		},
		add_todo_to_localstorage(todo) {
			var todos = JSON.parse(localStorage.getItem('todos'))
			todos.push(todo)
			localStorage.setItem('todos', JSON.stringify(todos))
		},
		remove_todo_from_localstorage(indice) {
			var todos = JSON.parse(localStorage.getItem('todos'))
			todos.splice(indice , 1)
			localStorage.setItem('todos', JSON.stringify(todos))
		}
	}

	function loadTodos(){
		todos = tododatabase.load_todos_from_localstorage()
		for(var i=0; i < todos.length; i++){
			addTodo(todos[i]);
		}
	}

	function addTodo(todo){
		var todoHTML = '<tr>';
		todoHTML += '<td class="todocheck"><input type="checkbox"' + (todo.done ? 'checked' : '') +'></td>';
		todoHTML += '<td class="js-todotodo ' + (todo.done ? 'tododone' : '') +'">'+ todo.todo +'</td>';
		todoHTML += '<td class="todoremove"><a href="#"><span class="glyphicon glyphicon-trash" aria-hidden="true"></span> </a></td>';
		todoHTML += '</tr>';
		var $todoHTML = $(todoHTML)
		instrument($todoHTML);
		$('#todotable').append($todoHTML)
	}

	function instrument($todo){
		var $checkbox = $todo.find('.todocheck input');
		var $removeIcon = $todo.find('.todoremove a');

		$checkbox.change(function(evt){
			var ischecked = evt.target.checked
			if(ischecked){
				$todo.find('.js-todotodo').addClass('tododone')
				//TODO: avisar o backend
			} else {
				$todo.find('.js-todotodo').removeClass('tododone')
				//TODO: avisar o backend
			}
		});

		$removeIcon.click(function(){
			var trs_irmaos = $todo.parent().children()
			for(var i = 0; i<trs_irmaos.length; i++){
				if (trs_irmaos[i] == $todo[0]) {
					break
				}
			}
			$todo.remove()
			tododatabase.remove_todo_from_localstorage(i)
			//TODO: avisar o backend
		});
	}

	function instrumentNewTask(){
		var $newtask = $('#newtask')
		$newtask.keyup(function(evt){
			if(evt.keyCode == 13){
				var todo = {
					todo: $newtask.val(),
					done: false
				}

				addTodo(todo);
				tododatabase.add_todo_to_localstorage(todo);
				$newtask.val('')
			}
		});
	}

	loadTodos();

	instrumentNewTask();
});
