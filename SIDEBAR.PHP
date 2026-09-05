<!--  Sidebar starting -->
        <!-- Sidebar  add this to class bg-gradient-primary-->
        <ul style="background-color:#852483" class="navbar-nav sidebar sidebar-dark accordion" id="accordionSidebar">

            <!-- Sidebar - Brand -->
            <a class="sidebar-brand d-flex align-items-center justify-content-center" href="index.php">
                <div class="sidebar-brand-icon rotate-n-15">
                    <!-- <i class="fas fa-laugh-wink"></i> -->
                </div>
                <div class="sidebar-brand-text mx-3"><img src="img/company_logo.png" > <sup></sup></div>
            </a>

            <!-- Divider -->
            <hr class="sidebar-divider my-0">

            <!-- Nav Item - Dashboard -->
            <li class="nav-item active">
                <a class="nav-link" href="index.php">
                    <i class="fas fa-fw fa-tachometer-alt"></i>
                    <span>Dashboard</span></a>
            </li>

            <!-- Divider -->
            <hr class="sidebar-divider">

            <!-- Heading -->
            <div class="sidebar-heading">
                Records
            </div>



            <!-- Nav Item - Pages Collapse Menu -->
            <li class="nav-item">

                <?php 

                    if( $_SESSION['id'] == 2 or $_SESSION['id'] == 1 )
                    {
                        
                       echo    "<a  class='nav-link collapsed' href='#' data-toggle='collapse' data-target='#collapseTwo'
                                    aria-expanded='true' aria-controls='collapseTwo'>
                                    <i class='fas fa-fw fa-cog'></i>
                                    <span>Cryo Vessels</span>
                                </a>";

                    }
                ?>

                    <div  id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordionSidebar">

                        <div  style="background-color:#852483" class=" py-2 collapse-inner rounded">


                            <a style="color:#00bbff" class="collapse-item"  href="index.php">MVE TEC</a>
                            <a style="color:#00bbff" class="collapse-item" href="#" data-toggle="modal" data-target="#multinode">
                                        <i class="fas fa-sign-out-alt fa-sm fa-fw mr-2 text-gray-400"></i>
                                Monitor MVE TEC 
                            </a>

                            <a style="color:#00bbff" class="collapse-item"  href="gold_sim.php">GOLD SIM</a>
                            <a style="color:#00bbff" class="collapse-item" href="#" data-toggle="modal" data-target="#multi_gold">
                                        <i class="fas fa-sign-out-alt fa-sm fa-fw mr-2 text-gray-400"></i>
                                Monitor GOLD SIM 
                            </a>

                            <a style="color:#00bbff" class="collapse-item"  href="twm.php">TAYLOR WHARTON</a>
                            <a style="color:#00bbff" class="collapse-item" href="#" data-toggle="modal" data-target="#multi_twm">
                                        <i class="fas fa-sign-out-alt fa-sm fa-fw mr-2 text-gray-400"></i>
                                Monitor TW
                            </a>

                            <a  style="color:#00bbff;font-size:16px" class="collapse-item"  href="all_vessels.php">All Vessels Data </a>

                        </div>
                    </div>
            </li>



            <li class="nav-item">

            <?php 

            if( $_SESSION['id'] == 1 )
            {
              echo  "<a  class='nav-link collapsed' href='#' data-toggle='collapse' data-target='#collapsesdw'
                    aria-expanded='true' aria-controls='collapseTwo'>
                    <i class='fas fa-fw fa-credit-card'></i>
                    <span>Cryo Room</span>
                </a>";
            }
            ?>
                <div  id="collapsesdw" class="collapse" aria-labelledby="headingTwo" data-parent="#accordionSidebar">

                <div  style="background-color:#852483" class=" py-2 collapse-inner rounded">

                        <a style="color:#00bbff" class="collapse-item"  href="smartivf.php">HOME</a>
                        <a style="color:#00bbff" class="collapse-item" href="#" data-toggle="modal" data-target="#multi_room">
                                    <i class="fas fa-sign-out-alt fa-sm fa-fw mr-2 text-gray-400"></i>
                            Monitor Room 
                        </a>
                    </div>
                </div>
            </li>


            <li class="nav-item">
            <?php 

            if( $_SESSION['id'] == 3 or $_SESSION['id'] == 1 )
            {                
                echo "<a  class='nav-link collapsed' href='#' data-toggle='collapse' data-target='#collapsepressure'
                    aria-expanded='true' aria-controls='collapseTwo'>
                    <i class='fas fa-fw fa-pen'></i>
                    <span>PTH Monitor </span>
                </a>";
            }
            ?>
                <div  id="collapsepressure" class="collapse" aria-labelledby="headingTwo" data-parent="#accordionSidebar">
                <!-- add it bg-white -->
                <div  style="background-color:#852483" class=" py-2 collapse-inner rounded">
                        <!-- <h6 class="collapse-header">Custom Components:</h6> -->

                        <a style="color:#00bbff" class="collapse-item"  href="pressure_room.php">HOME</a>
                        <a  style="color:#00bbff;font-size:16px" class="collapse-item"  href="all_pth_data.php">All PTH Data </a>
                        <a style="color:#00bbff" class="collapse-item" href="#" data-toggle="modal" data-target="#multi_pth">
                                    <i class="fas fa-sign-out-alt fa-sm fa-fw mr-2 text-gray-400"></i>
                            Monitor PTH
                        </a>                        
                    </div>
                </div>
            </li>




            <!-- Nav Item - Utilities Collapse Menu -->
            <li class="nav-item">
            <?php 

            if( $_SESSION['id'] == 1 )
            {                   
              echo  "<a class='nav-link collapsed' href='#' data-toggle='collapse' data-target='#collapseUtilities'
                    aria-expanded='true' aria-controls='collapseUtilities'>
                    <i class='fas fa-fw fa-wrench'></i>
                    <span>Freezer Temperature</span>
                    
                </a>";
            }
            ?>
                <div id="collapseUtilities" class="collapse" aria-labelledby="headingUtilities"
                    data-parent="#accordionSidebar">
                    <div style="background-color:#852483" class=" py-2 collapse-inner rounded">
                        <!-- <h6 class="collapse-header">Custom Utilities:</h6> -->
                        <a style="color:#00bbff" class="collapse-item" href="deep_freezer.php">HOME</a>
                        <a style="color:#00bbff" class="collapse-item" href="#" data-toggle="modal" data-target="#multi_freezer">
                                    <i class="fas fa-sign-out-alt fa-sm fa-fw mr-2 text-gray-400"></i>
                            Monitor Freezer 
                        </a>
                        <!-- <a class="collapse-item" href="utilities-border.php">Roboscope Data</a> -->
                        <!-- <a class="collapse-item" href="utilities-animation.php">Animations</a> -->
                        <!-- <a class="collapse-item" href="utilities-other.php">Other</a> -->
                    </div>
                </div>
            </li>

            <!-- Divider -->
            <!-- <hr class="sidebar-divider"> -->

            <!-- Heading -->
            <!-- <div class="sidebar-heading">
                Addons
            </div> -->





</br>
</br>
</br></br>
</br>
</br>
<!-- Sidebar Toggler (Sidebar) -->
            <div class="text-center d-none d-md-inline">
                <button class="rounded-circle border-0" id="sidebarToggle"></button>
            </div>

        </ul>

        <!-- end of  Sidebar -->
