-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 25 Paź 2023, 11:54
-- Wersja serwera: 10.4.25-MariaDB
-- Wersja PHP: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `trudnosci`
--

CREATE DATABASE `trudnosci`;
USE trudnosci;

--
-- Struktura tabeli dla tabeli `poziom1`
--

CREATE TABLE `poziom1` (
  `id` int(11) NOT NULL,
  `obrazek` text COLLATE utf8mb4_polish_ci NOT NULL,
  `odpowiedz` text COLLATE utf8mb4_polish_ci NOT NULL,
  `napis` text COLLATE utf8mb4_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_polish_ci;

--
-- Zrzut danych tabeli `poziom1`
--

INSERT INTO `poziom1` (`id`, `obrazek`, `odpowiedz`, `napis`) VALUES
(1, 'jabłko.png', 'omena', 'jabłko'),
(2, 'pomarancza.png', 'appelsiini', 'pomarańcza'),
(3, 'gruszka.png', 'päärynä', 'gruszka'),
(4, 'Banan.png', 'banaani', 'banan'),
(5, 'truskawka.png', 'mansikka', 'truskawka'),
(6, 'Cytryna.png', 'sitruuna', 'cytryna'),
(7, 'ziemniak.png', 'peruna', 'ziemniak'),
(8, 'Arbuz.png', 'vesi-melooni', 'arbuz'),
(9, 'marchewka.png', 'porkkana', 'marchewka'),
(10, 'rzodkiewka.png', 'retiisi', 'rzodkiewka'),
(11, 'kalarepa.png', 'kyssäkaali', 'kalarepa'),
(12, 'Por.png', 'purjo', 'por'),
(13, 'Kukurydza.png', 'maissi', 'kukurydza'),
(14, 'Burak.png', 'puna-juuri', 'burak'),
(15, 'Pomidor.png', 'tomaati', 'pomidor'),
(16, 'Groszek.png', 'herne', 'groszek'),
(17, 'ogórek.png', 'kurkku', 'ogórek'),
(18, 'pieczarki.png', 'herkku-sieeni', 'pieczarki'),
(19, 'Malina.png', 'vadelma', 'malina'),
(20, 'Pietruszka.png', 'persilja', 'pietruszka');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `poziom2`
--

CREATE TABLE `poziom2` (
  `id` int(11) NOT NULL,
  `napis` text COLLATE utf8mb4_polish_ci NOT NULL,
  `odpowiedz` text COLLATE utf8mb4_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_polish_ci;

--
-- Zrzut danych tabeli `poziom2`
--

INSERT INTO `poziom2` (`id`, `napis`, `odpowiedz`) VALUES
(1, 'jabłko', 'omena'),
(2, 'pomarańcza', 'appelsiini'),
(3, 'gruszka', 'päärynä'),
(4, 'banan', 'banaani'),
(5, 'truskawka', 'mansikka'),
(6, 'cytryna', 'sitruuna'),
(7, 'ziemniak', 'peruna'),
(8, 'arbuz', 'vesi-melooni'),
(9, 'marchewka', 'porkkana'),
(10, 'rzodkiewka', 'retiisi'),
(11, 'kalarepa', 'kyssäkaali'),
(12, 'por', 'purjo'),
(13, 'kukurydza', 'maissi'),
(14, 'burak', 'puna-juuri'),
(15, 'pomidor', 'tomaati'),
(16, 'groszek', 'herne'),
(17, 'ogórek', 'kurkku'),
(18, 'pieczarki', 'herkku-sieeni'),
(19, 'malina', 'vadelma'),
(20, 'pietruszka', 'persilja');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `poziom3`
--

CREATE TABLE `poziom3` (
  `id` int(11) NOT NULL,
  `napis_polski` text COLLATE utf8mb4_polish_ci NOT NULL,
  `fin_slowo` text COLLATE utf8mb4_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_polish_ci;

--
-- Zrzut danych tabeli `poziom3`
--

INSERT INTO `poziom3` (`id`, `napis_polski`, `fin_slowo`) VALUES
(1, 'jabłko', 'omena'),
(2, 'pomarańcza', 'appelsiini'),
(3, 'gruszka', 'päärynä'),
(4, 'banan', 'banaani'),
(5, 'truskawka', 'mansikka'),
(6, 'cytryna', 'sitruuna'),
(7, 'ziemniak', 'peruna'),
(8, 'arbuz', 'vesi-melooni'),
(9, 'marchewka', 'porkkana'),
(10, 'rzodkiewka', 'retiisi'),
(11, 'kalarepa', 'kyssäkaali'),
(12, 'por', 'purjo'),
(13, 'kukurydza', 'maissi'),
(14, 'burak', 'puna-juuri'),
(15, 'pomidor', 'tomaati'),
(16, 'groszek', 'herne'),
(17, 'ogórek', 'kurkku'),
(18, 'pieczarki', 'herkku-sieeni'),
(19, 'malina', 'vadelma'),
(20, 'pietruszka', 'persilja');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `poziom1`
--
ALTER TABLE `poziom1`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `poziom2`
--
ALTER TABLE `poziom2`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `poziom3`
--
ALTER TABLE `poziom3`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT dla zrzuconych tabel
--

--
-- AUTO_INCREMENT dla tabeli `poziom1`
--
ALTER TABLE `poziom1`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT dla tabeli `poziom2`
--
ALTER TABLE `poziom2`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT dla tabeli `poziom3`
--
ALTER TABLE `poziom3`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
