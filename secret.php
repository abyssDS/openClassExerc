<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8" />
	<title>Code d'accès au serveur central de la NASA</title>
</head>
<body>
	<?php
	if (isset($_POST['mot_de_passe']) AND $_POST['mot_de_passe'] == "Kangourou"){
	?>
	<h1>Voici les codes d'accès :</h1>
	<p><strong>CR88B-EB78G-HH3S0-A9BXB-JJKQ1</strong></p>
	<p>
		Cette page est réservée au personnel ... <br />
		La NASA vous remercie ...
	</p>
	<?php
}else
{
	echo '<p> Mot de passe incorrect </p>';
}
?>
</body>
</html>
