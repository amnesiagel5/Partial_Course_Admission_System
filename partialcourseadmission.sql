-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 19, 2020 at 02:28 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `partialcourseadmission`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbl_freshmen`
--

CREATE TABLE `tbl_freshmen` (
  `id` int(11) NOT NULL,
  `firstname` text NOT NULL,
  `mi` text NOT NULL,
  `lastname` text NOT NULL,
  `previousschool` text NOT NULL,
  `desiredcourse` text NOT NULL,
  `generalaverage` int(11) NOT NULL,
  `date` text NOT NULL,
  `time` text NOT NULL,
  `remarks` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_freshmen`
--

INSERT INTO `tbl_freshmen` (`id`, `firstname`, `mi`, `lastname`, `previousschool`, `desiredcourse`, `generalaverage`, `date`, `time`, `remarks`) VALUES
(1, 'Ken', 'S.', 'Kaneki', 'Tomoeda High School', 'Bachelor of Elementary Education (BEED)', 90, ' 5-19-2020 ', ' 18:31:0 ', 'Requirements are complete.\nQualified to enroll!'),
(3, 'Ingrid', 'T.', 'Ibarra', 'Philippine Science High School', 'Bachelor of Arts in Literature (AB-Lit)', 95, ' 5-18-2020 ', ' 15:39:3 ', 'Requirements are complete.\nQualified to enroll!'),
(4, 'Uriel', 'W.', 'Cio', 'Sisters of Mary (Boys Town)', 'Bachelor of Science in Industrial Engineering (BSIE)', 90, ' 5-18-2020 ', ' 15:49:8 ', 'Requirements are complete.\nQualified to enroll!');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_gradschool`
--

CREATE TABLE `tbl_gradschool` (
  `id` int(11) NOT NULL,
  `IDNumber` int(11) NOT NULL,
  `LastName` text NOT NULL,
  `FirstName` text NOT NULL,
  `MI` text NOT NULL,
  `DesiredCourse` text NOT NULL,
  `Remarks` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_gradschool`
--

INSERT INTO `tbl_gradschool` (`id`, `IDNumber`, `LastName`, `FirstName`, `MI`, `DesiredCourse`, `Remarks`) VALUES
(1, 476686, 'Sy', 'Cherry', 'O.', 'Master of Arts in Education major in English Language & Literature Teaching (MAed-ELLT)', 'Requirements are complete.\nQualified to enroll!'),
(2, 468, 'Geso', 'Anah', 'T.', 'Diploma / Certificate in Professional Education (DPE/CPE)', 'Incomplete Requirements.\nUnqualified to enroll!'),
(6, 12345, 'Minor', 'Deneb', 'R.', 'Master of Arts in Education major in Teaching Mathematics (MAEd-TM)', 'Requirements are complete.\nQualified to enroll!');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_oldstudents`
--

CREATE TABLE `tbl_oldstudents` (
  `id` int(11) NOT NULL,
  `LastName` text NOT NULL,
  `FirstName` text NOT NULL,
  `MI` text NOT NULL,
  `IDNumber` int(11) NOT NULL,
  `Course` text NOT NULL,
  `Program` text NOT NULL,
  `Year` varchar(20) NOT NULL,
  `Remarks` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_oldstudents`
--

INSERT INTO `tbl_oldstudents` (`id`, `LastName`, `FirstName`, `MI`, `IDNumber`, `Course`, `Program`, `Year`, `Remarks`) VALUES
(7, 'Han', 'Lizzy', 'O.', 345, 'Bachelor of Arts in Literature (AB-Lit)', 'Day', '3rd Year', 'Requirements are complete.\nQualified to enroll!'),
(17, 'Reyes', 'Suzy', 'H.', 7185678, 'Bachelor of Science in Forestry (BSF)', 'Day', '3rd Year', 'Requirements are complete.\nQualified to enroll!'),
(18, 'Go', 'Namshin', 'R.', 1234, 'Bachelor of Secondary Education major in Math (BSED-Math)', 'Day', '3rd Year', 'Incomplete Requirements.\nUnqualified to enroll!');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_secdegree`
--

CREATE TABLE `tbl_secdegree` (
  `id` int(11) NOT NULL,
  `fname` text NOT NULL,
  `mi` text NOT NULL,
  `lname` text NOT NULL,
  `desiredcourse` text NOT NULL,
  `dateadmission` text NOT NULL,
  `remarks` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_secdegree`
--

INSERT INTO `tbl_secdegree` (`id`, `fname`, `mi`, `lname`, `desiredcourse`, `dateadmission`, `remarks`) VALUES
(4, 'Suzy', 'E', 'Bae', '(BTLEd) Bachelor of Technology and Livelihood Education major in Home Economics', '5/19/2020', 'Incomplete Requirements.\nUnqualified to enroll!'),
(6, 'Shiki', 'A.', 'Yukamizo', '(BSA) Bachelor of Science in Agriculture major in Animal Science', '5/14/2020', 'Requirements are complete.\nQualified to enroll!'),
(7, 'Ursa', 'G.', 'Rosalia', '(BSHM) Bachelor of Science in Hospitality Management', '5/19/2020', 'Requirements are complete.\nQualified to enroll!'),
(8, 'Taki', 'T.', 'Tachibana', '(BIT-CT) Bachelor in Industrial Technology major in Computer Technology', '5/19/2020', 'Incomplete Requirements.\nUnqualified to enroll!');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_transferees`
--

CREATE TABLE `tbl_transferees` (
  `id` int(11) NOT NULL,
  `firstname` text NOT NULL,
  `mi` text NOT NULL,
  `lastname` text NOT NULL,
  `previousschool` text NOT NULL,
  `desiredcourse` text NOT NULL,
  `remarks` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_transferees`
--

INSERT INTO `tbl_transferees` (`id`, `firstname`, `mi`, `lastname`, `previousschool`, `desiredcourse`, `remarks`) VALUES
(4, 'Felix', 'Q.', 'Sy', 'Integrated High School', 'Bachelor of Science in Agriculture major in Crop Production (BSA)', 'Incomplete Requirements.\nUnqualified to enroll!'),
(6, 'George', 'T.', 'Hugo', 'Integrated High School', 'Bachelor of Secondary Education major in Math (BSED-Math)', 'Incomplete Requirements.\nUnqualified to enroll!'),
(8, 'Dan', 'G.', 'Oh', 'Simala National High School', 'Bachelor in Industrial Technology major in Automotive Technology (BIT-AT)', 'Incomplete Requirements.\nUnqualified to enroll!'),
(9, 'Cesar', 'S.', 'Yu', 'Brent International School', 'Bachelor of Technology and Livelihood Education major in Home Economics (BTLEd)', 'Requirements are complete.\nQualified to enroll!'),
(10, 'Nana', 'Q.', 'Koh', 'Brent International School', 'Bachelor of Science in Agriculture major in Animal Science (BSA)', 'Requirements are complete.\nQualified to enroll!');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbl_freshmen`
--
ALTER TABLE `tbl_freshmen`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_gradschool`
--
ALTER TABLE `tbl_gradschool`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_oldstudents`
--
ALTER TABLE `tbl_oldstudents`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_secdegree`
--
ALTER TABLE `tbl_secdegree`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_transferees`
--
ALTER TABLE `tbl_transferees`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_freshmen`
--
ALTER TABLE `tbl_freshmen`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `tbl_gradschool`
--
ALTER TABLE `tbl_gradschool`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tbl_oldstudents`
--
ALTER TABLE `tbl_oldstudents`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `tbl_secdegree`
--
ALTER TABLE `tbl_secdegree`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `tbl_transferees`
--
ALTER TABLE `tbl_transferees`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
