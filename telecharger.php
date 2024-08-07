<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $videoUrl = $_POST['videoUrl'];

    // Nettoyage du lien pour éviter les commandes malicieuses
    $videoUrl = escapeshellarg($videoUrl);

    // Dossier de sortie
    $outputDir = 'downloads/';
    if (!file_exists($outputDir)) {
        mkdir($outputDir, 0777, true);
    }

    // Commande pour télécharger la vidéo avec youtube-dl
    $command = "youtube-dl -o '" . $outputDir . "%(title)s.%(ext)s' " . $videoUrl;

    // Exécuter la commande
    $output = shell_exec($command);

    echo "<h2>Résultat du Téléchargement</h2>";
    echo "<pre>$output</pre>";

    // Vous pouvez ajouter un lien pour télécharger la vidéo localement
}
?>
