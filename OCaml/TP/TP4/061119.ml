type tas = {mutable n : int; t : int array};;

(*Q1*)

let exemple = {n=6;t= Array.make 50 0};;			
(exemple.t).(0) <- 5;;
(exemple.t).(1) <- 4;;
(exemple.t).(2) <- 3;;
(exemple.t).(3) <- 2;;
(exemple.t).(4) <- 1;;
(exemple.t).(5) <- 0;;

exemple;;

(*Q2*)

let echange tas i j = 
	let c = (tas.t).(i) in 
		(tas.t).(i) <- (tas.t).(j);
		(tas.t).(j) <- c;;

let rec monte tas k = match k with 
	|0 -> ()
	|k -> let indice_pere = (k-1)/2 in 
		   if (tas.t).(indice_pere) < (tas.t).(k) then 
		   	 	(echange tas indice_pere k;
		   		monte tas indice_pere;);;

let rec descend tas k = match k with 
	|k when 2*k + 1 >= tas.n -> ()
	|k -> let j = if 2*k+2 = tas.n || (tas.t).(2*k+1) >   (tas.t).(2*k+2) then 2*k+1 else 2*k+2 in if (tas.t).(k) < (tas.t).(j) then echange tas k j; descend tas j;;

(*Q3*)

let extraire tas = 
	let racine = (tas.t).(0) in 
	   tas.n <- tas.n - 1;
		echange tas 0 (tas.n);
		descend tas 0;
		racine;;

extraire exemple;;
exemple;;

(*Q4*)

let insertion tas x = 
	(tas.t).(tas.n) <- x;
	monte tas (tas.n);
	tas.n <- (tas.n) + 1;;

insertion exemple 6;;
exemple;;

(*Q5*)

let creation t =
	for t
			








