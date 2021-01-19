
import re
from collections import defaultdict

# html_doc = """
# <div id="lottable" data-ng-show="for_gstin.searchresult">
#                 <div class="row" style="margin-top: 15px;">
#                     <div class="col-sm-6">
#                         <h4>Search Result based on GSTIN/UIN : 19APYPM3846D1ZB</h4>
#                     </div>
#                     <!-- Back Button -->
#                     <!----><div class="col-md-6" ng-if="showBckBtn">
#                        <button type="button" class="btn btn-default pull-right" data-ng-bind="trans.LBL_BACK" ng-click="getPanDetailsPre()">Back</button>
#                 </div><!---->
#                     <!-- Back Button -->
#                 </div>
#                 <div class="tbl-format">
#                     <div class="row">
#                         <div class="inner">
#                             <div class="col-sm-4 col-xs-12">
#                                 <p><strong data-ng-bind="trans.LBL_LEAGAL_NAME_BUSI">Legal Name of Business</strong></p>
#                                 <p>PARTHA  MUKHOPADHYAY</p>
#                             </div>
#                             <!----><div class="col-sm-4 col-xs-12" data-ng-if="tradeFlag">
#                                 <p><strong data-ng-bind="trans.LBL_TRAD_NAME">Trade Name</strong></p>
#                                 <p>SENTEX,M/S GALAXY HONDA</p>
#                             </div><!---->
#                             <div class="col-sm-4 col-xs-12">
#
#                                 <p><strong>Effective Date of registration</strong></p>
#
#                                 <p>01/07/2017</p>
#                             </div>
#                         </div>
#                     </div>
#                     <div class="row  ">
#                         <div class="inner">
#                             <div class="col-sm-4 col-xs-12">
#
#                                 <p><strong data-ng-bind="trans.LBL_CONST_BUSI">Constitution of Business</strong></p>
#
#                                 <p>Proprietorship</p>
#                             </div>
#                             <div class="col-sm-4 col-xs-12">
#
#                                 <p><strong data-ng-bind="trans.LBL_GSTIN_STAT">GSTIN / UIN  Status</strong></p>
#
#                                 <p>Active</p>
#                             </div>
#                             <div class="col-sm-4 col-xs-12 taxpayer-info">
#                                 <p><strong data-ng-bind="trans.LBL_TAXPAYER_TYPE">Taxpayer Type</strong>
#                                     <span>
#                                         <i class="fa fa-info-circle" data-toggle="tooltip" data-original-title="You can collect GST and can issue Tax Invoice.<br> You can also get Input tax credit on your purchases from registered taxable person."> </i>
#                                     </span>
#                                 </p>
#                                 <p>Regular</p>
#                             </div>
#                         </div>
#                     </div>
#                     <div class="row  ">
#                         <div class="inner">
#                             <div class="col-sm-4 col-xs-12">
#                                 <p><strong data-ng-bind="trans.LBL_ADMINSTRATIVE_OFFICE">Administrative Office</strong></p>
#                                 <ul class="jurisdictList">
#                                     <!----><li data-ng-repeat="adm in searchTaxpre_Payload.admOfc track by $index">
#                                        (JURISDICTION - CENTER)</li><!----><li data-ng-repeat="adm in searchTaxpre_Payload.admOfc track by $index">
#                                        Commisionerate - KOLKATA-NORTH</li><!----><li data-ng-repeat="adm in searchTaxpre_Payload.admOfc track by $index">
#                                        Division - KALYANI - NADIA DIVISION</li><!----><li data-ng-repeat="adm in searchTaxpre_Payload.admOfc track by $index">
#                                        Range - RANGE-IV </li><!---->
#                                 </ul>
#                             </div>
#                             <div class="col-sm-4 col-xs-12">
#
#                                 <p><strong data-ng-bind="trans.LBL_OTHER_OFFICE">Other Office</strong></p>
#                                 <ul class="jurisdictList">
#                                     <!----><li data-ng-repeat="othr in searchTaxpre_Payload.othrOfc track by $index">
#                                        (JURISDICTION - STATE)</li><!----><li data-ng-repeat="othr in searchTaxpre_Payload.othrOfc track by $index">
#                                        Commisionerate - West Bengal</li><!----><li data-ng-repeat="othr in searchTaxpre_Payload.othrOfc track by $index">
#                                        Circle - BAHARAMPUR</li><!----><li data-ng-repeat="othr in searchTaxpre_Payload.othrOfc track by $index">
#                                        Charge - KRISHNANAGAR</li><!---->
#                                 </ul>
#
#                             </div>
#                             <div class="col-sm-4 col-xs-12">
#                                 <p><strong data-ng-bind="trans.LBL_PRIN_PLAC">Principal Place of Business</strong></p>
#                                 <p class="wordCls" data-ng-bind="searchTaxpre_Payload.pradr.adr">4, MAITRA PARA LANE, SANTIPUR, Nadia, West Bengal, 741404</p>
#                             </div>
#                         </div>
#                     </div>
#
#                     <div class="row  ">
#                         <div class="inner">
#                             <div class="col-sm-4 col-xs-12">
#                                 <p><strong data-ng-bind="trans.LBL_DATE_CANC">Effective Date of Cancellation</strong></p>
#                                 <p></p>
#                             </div>
#                         </div>
#                     </div>
#                 </div>
#                 <div class="row" style="margin-top:20px;">
#                     <div class="inner">
#
#                         <div class="col-sm-12">
#                             <div class="panel panel-default">
#                                 <div class="panel-heading">
#                                     <h4 class="panel-title" data-toggle="collapse" data-parent="#accordion" href="#collapseTwo">
#                                                 <span class="fa fa-angle-up pull-right"></span>
#                     <p data-ng-bind="trans.LBL_NATURE_BUSI_ACTI">Nature of Business Activities</p>
#
#                 </h4>
#                                 </div>
#                                 <div id="collapseTwo" class="panel-collapse collapse in">
#                                     <div class="panel-body">
#                                         <ul class="list-child-inline">
#                                             <!---->
#                                             <!----><!----><li data-ng-if="!nba" data-ng-repeat="nature in searchTaxpre_Payload.nba track by $index">
#                                                 <span>1.
#                                                 </span>Retail Business</li><!----><!----><!----><li data-ng-if="!nba" data-ng-repeat="nature in searchTaxpre_Payload.nba track by $index">
#                                                 <span>2.
#                                                 </span>Wholesale Business</li><!----><!----><!----><li data-ng-if="!nba" data-ng-repeat="nature in searchTaxpre_Payload.nba track by $index">
#                                                 <span>3.
#                                                 </span>Warehouse / Depot</li><!----><!---->
#                                         </ul>
#                                     </div>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                 </div>
#                 <div class="row">
#                     <div class="col-sm-12">
#                         <div class="table-responsive">
#                             <h4>Dealing In Goods and Services</h4>
#                             <!----><div ng-if="!goodServErrMsg">
#                                 <table class="table tbl inv exp table-bordered">
#                                     <thead>
#                                         <tr>
#                                             <th class="headerWidth" colspan="2">Goods</th>
#                                             <th class="headerWidth" colspan="2">Services</th>
#                                         </tr>
#                                     </thead>
#                                     <tbody>
#                                         <tr>
#                                             <td>HSN</td>
#                                             <td>Description</td>
#                                             <td>HSN</td>
#                                             <td>Description</td>
#                                         </tr>
#                                         <!----><!----><tr data-ng-repeat="gd in modifiedGDServArr" data-ng-if="modifiedGDServArr.length">
#                                             <td>5303</td>
#                                             <td>JUTE AND OTHER TEXTILE BAST FIBRES (EXCLUDING FLAX, TRUE HEMP AND RAMIE), RAW OR PROCESSED BUT NOT SPUN; TOW AND WASTE OF THESE FIBRES (INCLUDING YARN WASTE AND GARNETTED STOCK)</td>
#                                             <td></td>
#                                             <td></td>
#                                         </tr><!----><!----><!----><tr data-ng-repeat="gd in modifiedGDServArr" data-ng-if="modifiedGDServArr.length">
#                                             <td>39171010</td>
#                                             <td>TUBES, PIPES AND HOSES, AND FITTINGS THEREFOR (FOR EXAMPLE, JOINTS, ELBOWS, FLANGES), OF PLASTICS - ARTIFICIAL GUTS (SAUSAGE CASINGS) OF HARDENED PROTEIN OR OF CELLULOSIC MATERIALS: OF HARDENED PROTEIN</td>
#                                             <td></td>
#                                             <td></td>
#                                         </tr><!----><!----><!----><tr data-ng-repeat="gd in modifiedGDServArr" data-ng-if="modifiedGDServArr.length">
#                                             <td>73101010</td>
#                                             <td>TANKS, CASKS, DRUMS, CANS, BOXES AND SIMILAR CONTAINERS, FOR ANY MATERIAL (OTHER THAN COMPRESSED OR LIQUEFIED GAS), OF IRON OR STEEL, OF A CAPACITY NOT EXCEEDING 300 L, WHETHER OR NOT LINED OR HEATINSULATED, BUT NOT FITTED WITH MECHANICAL OR THERMAL EQUIPMENT- OF A CAPACITY OF 50 L OR MORE : TIN PLATE CONTAINERS</td>
#                                             <td></td>
#                                             <td></td>
#                                         </tr><!----><!---->
#                                         <!---->
#                                     </tbody>
#                                 </table>
#                                 <p><strong>HSN: </strong>Harmonized System of Nomenclature of Goods and Services</p>
#                             </div><!---->
#                             <!---->
#                         </div>
#                     </div>
#                 </div>
#                 <div class="row">
#                     <div class="col-sm-3 col-xs-12">
#                         <button class="btn btn-primary " id="filingTable" data-ng-click="getFilingData('prelogin')" data-ng-disabled="fileData" disabled="disabled">Show Filing Table</button>
#                     </div>
#                 </div>
#                 <!----><div data-ng-if="filingStatus_payload">
#                 <div class="row" style="margin-top: 15px;">
# 			         <div class="col-sm-6">
# 				     <h4>Search Result based on GSTIN/UIN :  19APYPM3846D1ZB</h4>
# 			         </div>
#                 </div>
#                         <div class="safariWid row display-flex">
# 				    <!----><div class="col-sm-6" data-ng-repeat="rType in fillingValues">
#                         <div class="table-responsive">
#                                 <h4>Filing details for GSTR3B</h4>
#                             <table class="table tbl inv exp table-bordered ng-table" data-ng-table="listOfStatus"><!----><thead ng-include="templates.header"><!---->
# <tr class="ng-table-sort-header">
#     <!----><!----><th title="" ng-repeat="$column in $columns" ng-class="{
#                     'sortable': $column.sortable(this),
#                     'sort-asc': params.sorting()[$column.sortable(this)]=='asc',
#                     'sort-desc': params.sorting()[$column.sortable(this)]=='desc'
#                   }" ng-click="sortBy($column, $event)" ng-if="$column.show(this)" ng-init="template = $column.headerTemplateURL(this)" class="header ">
#         <!----><div ng-if="!template" class="ng-table-header" ng-class="{'sort-indicator': params.settings().sortingIndicator == 'div'}">
#             <span ng-bind="$column.title(this)" ng-class="{'sort-indicator': params.settings().sortingIndicator == 'span'}" class="sort-indicator">Financial Year</span>
#         </div><!---->
#         <!---->
#     </th><!----><!----><!----><th title="" ng-repeat="$column in $columns" ng-class="{
#                     'sortable': $column.sortable(this),
#                     'sort-asc': params.sorting()[$column.sortable(this)]=='asc',
#                     'sort-desc': params.sorting()[$column.sortable(this)]=='desc'
#                   }" ng-click="sortBy($column, $event)" ng-if="$column.show(this)" ng-init="template = $column.headerTemplateURL(this)" class="header ">
#         <!----><div ng-if="!template" class="ng-table-header" ng-class="{'sort-indicator': params.settings().sortingIndicator == 'div'}">
#             <span ng-bind="$column.title(this)" ng-class="{'sort-indicator': params.settings().sortingIndicator == 'span'}" class="sort-indicator">Tax Period</span>
#         </div><!---->
#         <!---->
#     </th><!----><!----><!----><th title="" ng-repeat="$column in $columns" ng-class="{
#                     'sortable': $column.sortable(this),
#                     'sort-asc': params.sorting()[$column.sortable(this)]=='asc',
#                     'sort-desc': params.sorting()[$column.sortable(this)]=='desc'
#                   }" ng-click="sortBy($column, $event)" ng-if="$column.show(this)" ng-init="template = $column.headerTemplateURL(this)" class="header ">
#         <!----><div ng-if="!template" class="ng-table-header" ng-class="{'sort-indicator': params.settings().sortingIndicator == 'div'}">
#             <span ng-bind="$column.title(this)" ng-class="{'sort-indicator': params.settings().sortingIndicator == 'span'}" class="sort-indicator">Date of filing</span>
#         </div><!---->
#         <!---->
#     </th><!----><!----><!----><th title="" ng-repeat="$column in $columns" ng-class="{
#                     'sortable': $column.sortable(this),
#                     'sort-asc': params.sorting()[$column.sortable(this)]=='asc',
#                     'sort-desc': params.sorting()[$column.sortable(this)]=='desc'
#                   }" ng-click="sortBy($column, $event)" ng-if="$column.show(this)" ng-init="template = $column.headerTemplateURL(this)" class="header ">
#         <!----><div ng-if="!template" class="ng-table-header" ng-class="{'sort-indicator': params.settings().sortingIndicator == 'div'}">
#             <span ng-bind="$column.title(this)" ng-class="{'sort-indicator': params.settings().sortingIndicator == 'span'}" class="sort-indicator">Status</span>
#         </div><!---->
#         <!---->
#     </th><!----><!---->
# </tr>
# <tr ng-show="show_filter" class="ng-table-filters ng-hide">
#     <!----><!----><th data-title-text="Financial Year" ng-repeat="$column in $columns" ng-if="$column.show(this)" class="filter " ng-class="params.settings().filterOptions.filterLayout === 'horizontal' ? 'filter-horizontal' : ''">
#         <!---->
#     </th><!----><!----><!----><th data-title-text="Tax Period" ng-repeat="$column in $columns" ng-if="$column.show(this)" class="filter " ng-class="params.settings().filterOptions.filterLayout === 'horizontal' ? 'filter-horizontal' : ''">
#         <!---->
#     </th><!----><!----><!----><th data-title-text="Date of filing" ng-repeat="$column in $columns" ng-if="$column.show(this)" class="filter " ng-class="params.settings().filterOptions.filterLayout === 'horizontal' ? 'filter-horizontal' : ''">
#         <!---->
#     </th><!----><!----><!----><th data-title-text="Status" ng-repeat="$column in $columns" ng-if="$column.show(this)" class="filter " ng-class="params.settings().filterOptions.filterLayout === 'horizontal' ? 'filter-horizontal' : ''">
#         <!---->
#     </th><!----><!---->
# </tr>
# </thead>
#                                 <tbody>
#                                         <!----><tr data-ng-repeat="y in $data[0][rType] | orderBy:['-fy','-orderVal']">
#                                         <td class="text-center" data-title="trans.HEAD_FINAN_YEAR" data-title-text="Financial Year">2020-2021</td>
#                                         <td class="text-center" data-title="trans.LBL_RET_FILING_PERIOD" data-title-text="Tax Period">October</td>
#                                         <td class="text-center" data-title="trans.LBL_DT_OF_FILING" data-title-text="Date of filing">24/11/2020</td>
#                                         <td class="text-center" data-title="trans.HEAD_FIL_STAT" data-title-text="Status">Filed</td>
#                                 </tr><!----><tr data-ng-repeat="y in $data[0][rType] | orderBy:['-fy','-orderVal']">
#                                         <td class="text-center" data-title="trans.HEAD_FINAN_YEAR" data-title-text="Financial Year">2020-2021</td>
#                                         <td class="text-center" data-title="trans.LBL_RET_FILING_PERIOD" data-title-text="Tax Period">September</td>
#                                         <td class="text-center" data-title="trans.LBL_DT_OF_FILING" data-title-text="Date of filing">19/10/2020</td>
#                                         <td class="text-center" data-title="trans.HEAD_FIL_STAT" data-title-text="Status">Filed</td>
#                                 </tr><!----><tr data-ng-repeat="y in $data[0][rType] | orderBy:['-fy','-orderVal']">
#                                         <td class="text-center" data-title="trans.HEAD_FINAN_YEAR" data-title-text="Financial Year">2020-2021</td>
#                                         <td class="text-center" data-title="trans.LBL_RET_FILING_PERIOD" data-title-text="Tax Period">August</td>
#                                         <td class="text-center" data-title="trans.LBL_DT_OF_FILING" data-title-text="Date of filing">19/10/2020</td>
#                                         <td class="text-center" data-title="trans.HEAD_FIL_STAT" data-title-text="Status">Filed</td>
#                                 </tr><!----><tr data-ng-repeat="y in $data[0][rType] | orderBy:['-fy','-orderVal']">
#                                         <td class="text-center" data-title="trans.HEAD_FINAN_YEAR" data-title-text="Financial Year">2020-2021</td>
#                                         <td class="text-center" data-title="trans.LBL_RET_FILING_PERIOD" data-title-text="Tax Period">July</td>
#                                         <td class="text-center" data-title="trans.LBL_DT_OF_FILING" data-title-text="Date of filing">18/10/2020</td>
#                                         <td class="text-center" data-title="trans.HEAD_FIL_STAT" data-title-text="Status">Filed</td>
#                                 </tr><!----><tr data-ng-repeat="y in $data[0][rType] | orderBy:['-fy','-orderVal']">
#                                         <td class="text-center" data-title="trans.HEAD_FINAN_YEAR" data-title-text="Financial Year">2020-2021</td>
#                                         <td class="text-center" data-title="trans.LBL_RET_FILING_PERIOD" data-title-text="Tax Period">June</td>
#                                         <td class="text-center" data-title="trans.LBL_DT_OF_FILING" data-title-text="Date of filing">18/10/2020</td>
#                                         <td class="text-center" data-title="trans.HEAD_FIL_STAT" data-title-text="Status">Filed</td>
#                                 </tr><!----><tr data-ng-repeat="y in $data[0][rType] | orderBy:['-fy','-orderVal']">
#                                         <td class="text-center" data-title="trans.HEAD_FINAN_YEAR" data-title-text="Financial Year">2020-2021</td>
#                                         <td class="text-center" data-title="trans.LBL_RET_FILING_PERIOD" data-title-text="Tax Period">May</td>
#                                         <td class="text-center" data-title="trans.LBL_DT_OF_FILING" data-title-text="Date of filing">18/10/2020</td>
#                                         <td class="text-center" data-title="trans.HEAD_FIL_STAT" data-title-text="Status">Filed</td>
#                                 </tr><!----><tr data-ng-repeat="y in $data[0][rType] | orderBy:['-fy','-orderVal']">
#                                         <td class="text-center" data-title="trans.HEAD_FINAN_YEAR" data-title-text="Financial Year">2020-2021</td>
#                                         <td class="text-center" data-title="trans.LBL_RET_FILING_PERIOD" data-title-text="Tax Period">April</td>
#                                         <td class="text-center" data-title="trans.LBL_DT_OF_FILING" data-title-text="Date of filing">16/10/2020</td>
#                                         <td class="text-center" data-title="trans.HEAD_FIL_STAT" data-title-text="Status">Filed</td>
#                                 </tr><!----><tr data-ng-repeat="y in $data[0][rType] | orderBy:['-fy','-orderVal']">
#                                         <td class="text-center" data-title="trans.HEAD_FINAN_YEAR" data-title-text="Financial Year">2019-2020</td>
#                                         <td class="text-center" data-title="trans.LBL_RET_FILING_PERIOD" data-title-text="Tax Period">March</td>
#                                         <td class="text-center" data-title="trans.LBL_DT_OF_FILING" data-title-text="Date of filing">01/09/2020</td>
#                                         <td class="text-center" data-title="trans.HEAD_FIL_STAT" data-title-text="Status">Filed</td>
#                                 </tr><!----><tr data-ng-repeat="y in $data[0][rType] | orderBy:['-fy','-orderVal']">
#                                         <td class="text-center" data-title="trans.HEAD_FINAN_YEAR" data-title-text="Financial Year">2019-2020</td>
#                                         <td class="text-center" data-title="trans.LBL_RET_FILING_PERIOD" data-title-text="Tax Period">February</td>
#                                         <td class="text-center" data-title="trans.LBL_DT_OF_FILING" data-title-text="Date of filing">24/03/2020</td>
#                                         <td class="text-center" data-title="trans.HEAD_FIL_STAT" data-title-text="Status">Filed</td>
#                                 </tr><!----><tr data-ng-repeat="y in $data[0][rType] | orderBy:['-fy','-orderVal']">
#                                         <td class="text-center" data-title="trans.HEAD_FINAN_YEAR" data-title-text="Financial Year">2019-2020</td>
#                                         <td class="text-center" data-title="trans.LBL_RET_FILING_PERIOD" data-title-text="Tax Period">January</td>
#                                         <td class="text-center" data-title="trans.LBL_DT_OF_FILING" data-title-text="Date of filing">24/02/2020</td>
#                                         <td class="text-center" data-title="trans.HEAD_FIL_STAT" data-title-text="Status">Filed</td>
#                                 </tr><!---->
#                             </tbody>
#                         </table><div ng-table-pagination="params" template-url="templates.pagination"><!----><div ng-include="templateUrl"><!----><div class="ng-table-pager" ng-if="params.data.length">
#     <!---->
#     <!---->
# </div><!---->
# </div></div>
# 				        </div>
# 				    </div><!----><div class="col-sm-6" data-ng-repeat="rType in fillingValues">
#                         <div class="table-responsive">
#                                 <h4>Filing details for GSTR1</h4>
#                             <table class="table tbl inv exp table-bordered ng-table" data-ng-table="listOfStatus"><!----><thead ng-include="templates.header"><!---->
# <tr class="ng-table-sort-header">
#     <!----><!----><th title="" ng-repeat="$column in $columns" ng-class="{
#                     'sortable': $column.sortable(this),
#                     'sort-asc': params.sorting()[$column.sortable(this)]=='asc',
#                     'sort-desc': params.sorting()[$column.sortable(this)]=='desc'
#                   }" ng-click="sortBy($column, $event)" ng-if="$column.show(this)" ng-init="template = $column.headerTemplateURL(this)" class="header ">
#         <!----><div ng-if="!template" class="ng-table-header" ng-class="{'sort-indicator': params.settings().sortingIndicator == 'div'}">
#             <span ng-bind="$column.title(this)" ng-class="{'sort-indicator': params.settings().sortingIndicator == 'span'}" class="sort-indicator">Financial Year</span>
#         </div><!---->
#         <!---->
#     </th><!----><!----><!----><th title="" ng-repeat="$column in $columns" ng-class="{
#                     'sortable': $column.sortable(this),
#                     'sort-asc': params.sorting()[$column.sortable(this)]=='asc',
#                     'sort-desc': params.sorting()[$column.sortable(this)]=='desc'
#                   }" ng-click="sortBy($column, $event)" ng-if="$column.show(this)" ng-init="template = $column.headerTemplateURL(this)" class="header ">
#         <!----><div ng-if="!template" class="ng-table-header" ng-class="{'sort-indicator': params.settings().sortingIndicator == 'div'}">
#             <span ng-bind="$column.title(this)" ng-class="{'sort-indicator': params.settings().sortingIndicator == 'span'}" class="sort-indicator">Tax Period</span>
#         </div><!---->
#         <!---->
#     </th><!----><!----><!----><th title="" ng-repeat="$column in $columns" ng-class="{
#                     'sortable': $column.sortable(this),
#                     'sort-asc': params.sorting()[$column.sortable(this)]=='asc',
#                     'sort-desc': params.sorting()[$column.sortable(this)]=='desc'
#                   }" ng-click="sortBy($column, $event)" ng-if="$column.show(this)" ng-init="template = $column.headerTemplateURL(this)" class="header ">
#         <!----><div ng-if="!template" class="ng-table-header" ng-class="{'sort-indicator': params.settings().sortingIndicator == 'div'}">
#             <span ng-bind="$column.title(this)" ng-class="{'sort-indicator': params.settings().sortingIndicator == 'span'}" class="sort-indicator">Date of filing</span>
#         </div><!---->
#         <!---->
#     </th><!----><!----><!----><th title="" ng-repeat="$column in $columns" ng-class="{
#                     'sortable': $column.sortable(this),
#                     'sort-asc': params.sorting()[$column.sortable(this)]=='asc',
#                     'sort-desc': params.sorting()[$column.sortable(this)]=='desc'
#                   }" ng-click="sortBy($column, $event)" ng-if="$column.show(this)" ng-init="template = $column.headerTemplateURL(this)" class="header ">
#         <!----><div ng-if="!template" class="ng-table-header" ng-class="{'sort-indicator': params.settings().sortingIndicator == 'div'}">
#             <span ng-bind="$column.title(this)" ng-class="{'sort-indicator': params.settings().sortingIndicator == 'span'}" class="sort-indicator">Status</span>
#         </div><!---->
#         <!---->
#     </th><!----><!---->
# </tr>
# <tr ng-show="show_filter" class="ng-table-filters ng-hide">
#     <!----><!----><th data-title-text="Financial Year" ng-repeat="$column in $columns" ng-if="$column.show(this)" class="filter " ng-class="params.settings().filterOptions.filterLayout === 'horizontal' ? 'filter-horizontal' : ''">
#         <!---->
#     </th><!----><!----><!----><th data-title-text="Tax Period" ng-repeat="$column in $columns" ng-if="$column.show(this)" class="filter " ng-class="params.settings().filterOptions.filterLayout === 'horizontal' ? 'filter-horizontal' : ''">
#         <!---->
#     </th><!----><!----><!----><th data-title-text="Date of filing" ng-repeat="$column in $columns" ng-if="$column.show(this)" class="filter " ng-class="params.settings().filterOptions.filterLayout === 'horizontal' ? 'filter-horizontal' : ''">
#         <!---->
#     </th><!----><!----><!----><th data-title-text="Status" ng-repeat="$column in $columns" ng-if="$column.show(this)" class="filter " ng-class="params.settings().filterOptions.filterLayout === 'horizontal' ? 'filter-horizontal' : ''">
#         <!---->
#     </th><!----><!---->
# </tr>
# </thead>
#                                 <tbody>
#                                         <!----><tr data-ng-repeat="y in $data[0][rType] | orderBy:['-fy','-orderVal']">
#                                         <td class="text-center" data-title="trans.HEAD_FINAN_YEAR" data-title-text="Financial Year">2020-2021</td>
#                                         <td class="text-center" data-title="trans.LBL_RET_FILING_PERIOD" data-title-text="Tax Period">June</td>
#                                         <td class="text-center" data-title="trans.LBL_DT_OF_FILING" data-title-text="Date of filing">19/10/2020</td>
#                                         <td class="text-center" data-title="trans.HEAD_FIL_STAT" data-title-text="Status">Filed</td>
#                                 </tr><!----><tr data-ng-repeat="y in $data[0][rType] | orderBy:['-fy','-orderVal']">
#                                         <td class="text-center" data-title="trans.HEAD_FINAN_YEAR" data-title-text="Financial Year">2019-2020</td>
#                                         <td class="text-center" data-title="trans.LBL_RET_FILING_PERIOD" data-title-text="Tax Period">March</td>
#                                         <td class="text-center" data-title="trans.LBL_DT_OF_FILING" data-title-text="Date of filing">11/10/2020</td>
#                                         <td class="text-center" data-title="trans.HEAD_FIL_STAT" data-title-text="Status">Filed</td>
#                                 </tr><!----><tr data-ng-repeat="y in $data[0][rType] | orderBy:['-fy','-orderVal']">
#                                         <td class="text-center" data-title="trans.HEAD_FINAN_YEAR" data-title-text="Financial Year">2019-2020</td>
#                                         <td class="text-center" data-title="trans.LBL_RET_FILING_PERIOD" data-title-text="Tax Period">February</td>
#                                         <td class="text-center" data-title="trans.LBL_DT_OF_FILING" data-title-text="Date of filing">11/10/2020</td>
#                                         <td class="text-center" data-title="trans.HEAD_FIL_STAT" data-title-text="Status">Filed</td>
#                                 </tr><!----><tr data-ng-repeat="y in $data[0][rType] | orderBy:['-fy','-orderVal']">
#                                         <td class="text-center" data-title="trans.HEAD_FINAN_YEAR" data-title-text="Financial Year">2019-2020</td>
#                                         <td class="text-center" data-title="trans.LBL_RET_FILING_PERIOD" data-title-text="Tax Period">January</td>
#                                         <td class="text-center" data-title="trans.LBL_DT_OF_FILING" data-title-text="Date of filing">11/10/2020</td>
#                                         <td class="text-center" data-title="trans.HEAD_FIL_STAT" data-title-text="Status">Filed</td>
#                                 </tr><!----><tr data-ng-repeat="y in $data[0][rType] | orderBy:['-fy','-orderVal']">
#                                         <td class="text-center" data-title="trans.HEAD_FINAN_YEAR" data-title-text="Financial Year">2019-2020</td>
#                                         <td class="text-center" data-title="trans.LBL_RET_FILING_PERIOD" data-title-text="Tax Period">December</td>
#                                         <td class="text-center" data-title="trans.LBL_DT_OF_FILING" data-title-text="Date of filing">11/10/2020</td>
#                                         <td class="text-center" data-title="trans.HEAD_FIL_STAT" data-title-text="Status">Filed</td>
#                                 </tr><!----><tr data-ng-repeat="y in $data[0][rType] | orderBy:['-fy','-orderVal']">
#                                         <td class="text-center" data-title="trans.HEAD_FINAN_YEAR" data-title-text="Financial Year">2019-2020</td>
#                                         <td class="text-center" data-title="trans.LBL_RET_FILING_PERIOD" data-title-text="Tax Period">November</td>
#                                         <td class="text-center" data-title="trans.LBL_DT_OF_FILING" data-title-text="Date of filing">11/10/2020</td>
#                                         <td class="text-center" data-title="trans.HEAD_FIL_STAT" data-title-text="Status">Filed</td>
#                                 </tr><!----><tr data-ng-repeat="y in $data[0][rType] | orderBy:['-fy','-orderVal']">
#                                         <td class="text-center" data-title="trans.HEAD_FINAN_YEAR" data-title-text="Financial Year">2019-2020</td>
#                                         <td class="text-center" data-title="trans.LBL_RET_FILING_PERIOD" data-title-text="Tax Period">October</td>
#                                         <td class="text-center" data-title="trans.LBL_DT_OF_FILING" data-title-text="Date of filing">11/10/2020</td>
#                                         <td class="text-center" data-title="trans.HEAD_FIL_STAT" data-title-text="Status">Filed</td>
#                                 </tr><!----><tr data-ng-repeat="y in $data[0][rType] | orderBy:['-fy','-orderVal']">
#                                         <td class="text-center" data-title="trans.HEAD_FINAN_YEAR" data-title-text="Financial Year">2019-2020</td>
#                                         <td class="text-center" data-title="trans.LBL_RET_FILING_PERIOD" data-title-text="Tax Period">September</td>
#                                         <td class="text-center" data-title="trans.LBL_DT_OF_FILING" data-title-text="Date of filing">11/10/2020</td>
#                                         <td class="text-center" data-title="trans.HEAD_FIL_STAT" data-title-text="Status">Filed</td>
#                                 </tr><!----><tr data-ng-repeat="y in $data[0][rType] | orderBy:['-fy','-orderVal']">
#                                         <td class="text-center" data-title="trans.HEAD_FINAN_YEAR" data-title-text="Financial Year">2019-2020</td>
#                                         <td class="text-center" data-title="trans.LBL_RET_FILING_PERIOD" data-title-text="Tax Period">August</td>
#                                         <td class="text-center" data-title="trans.LBL_DT_OF_FILING" data-title-text="Date of filing">11/10/2020</td>
#                                         <td class="text-center" data-title="trans.HEAD_FIL_STAT" data-title-text="Status">Filed</td>
#                                 </tr><!----><tr data-ng-repeat="y in $data[0][rType] | orderBy:['-fy','-orderVal']">
#                                         <td class="text-center" data-title="trans.HEAD_FINAN_YEAR" data-title-text="Financial Year">2019-2020</td>
#                                         <td class="text-center" data-title="trans.LBL_RET_FILING_PERIOD" data-title-text="Tax Period">July</td>
#                                         <td class="text-center" data-title="trans.LBL_DT_OF_FILING" data-title-text="Date of filing">11/10/2020</td>
#                                         <td class="text-center" data-title="trans.HEAD_FIL_STAT" data-title-text="Status">Filed</td>
#                                 </tr><!---->
#                             </tbody>
#                         </table><div ng-table-pagination="params" template-url="templates.pagination"><!----><div ng-include="templateUrl"><!----><div class="ng-table-pager" ng-if="params.data.length">
#     <!---->
#     <!---->
# </div><!---->
# </div></div>
# 				        </div>
# 				    </div><!----><div class="col-sm-6" data-ng-repeat="rType in fillingValues">
#                         <div class="table-responsive">
#                                 <h4>Filing details for GSTR9</h4>
#                             <table class="table tbl inv exp table-bordered ng-table" data-ng-table="listOfStatus"><!----><thead ng-include="templates.header"><!---->
# <tr class="ng-table-sort-header">
#     <!----><!----><th title="" ng-repeat="$column in $columns" ng-class="{
#                     'sortable': $column.sortable(this),
#                     'sort-asc': params.sorting()[$column.sortable(this)]=='asc',
#                     'sort-desc': params.sorting()[$column.sortable(this)]=='desc'
#                   }" ng-click="sortBy($column, $event)" ng-if="$column.show(this)" ng-init="template = $column.headerTemplateURL(this)" class="header ">
#         <!----><div ng-if="!template" class="ng-table-header" ng-class="{'sort-indicator': params.settings().sortingIndicator == 'div'}">
#             <span ng-bind="$column.title(this)" ng-class="{'sort-indicator': params.settings().sortingIndicator == 'span'}" class="sort-indicator">Financial Year</span>
#         </div><!---->
#         <!---->
#     </th><!----><!----><!----><th title="" ng-repeat="$column in $columns" ng-class="{
#                     'sortable': $column.sortable(this),
#                     'sort-asc': params.sorting()[$column.sortable(this)]=='asc',
#                     'sort-desc': params.sorting()[$column.sortable(this)]=='desc'
#                   }" ng-click="sortBy($column, $event)" ng-if="$column.show(this)" ng-init="template = $column.headerTemplateURL(this)" class="header ">
#         <!----><div ng-if="!template" class="ng-table-header" ng-class="{'sort-indicator': params.settings().sortingIndicator == 'div'}">
#             <span ng-bind="$column.title(this)" ng-class="{'sort-indicator': params.settings().sortingIndicator == 'span'}" class="sort-indicator">Tax Period</span>
#         </div><!---->
#         <!---->
#     </th><!----><!----><!----><th title="" ng-repeat="$column in $columns" ng-class="{
#                     'sortable': $column.sortable(this),
#                     'sort-asc': params.sorting()[$column.sortable(this)]=='asc',
#                     'sort-desc': params.sorting()[$column.sortable(this)]=='desc'
#                   }" ng-click="sortBy($column, $event)" ng-if="$column.show(this)" ng-init="template = $column.headerTemplateURL(this)" class="header ">
#         <!----><div ng-if="!template" class="ng-table-header" ng-class="{'sort-indicator': params.settings().sortingIndicator == 'div'}">
#             <span ng-bind="$column.title(this)" ng-class="{'sort-indicator': params.settings().sortingIndicator == 'span'}" class="sort-indicator">Date of filing</span>
#         </div><!---->
#         <!---->
#     </th><!----><!----><!----><th title="" ng-repeat="$column in $columns" ng-class="{
#                     'sortable': $column.sortable(this),
#                     'sort-asc': params.sorting()[$column.sortable(this)]=='asc',
#                     'sort-desc': params.sorting()[$column.sortable(this)]=='desc'
#                   }" ng-click="sortBy($column, $event)" ng-if="$column.show(this)" ng-init="template = $column.headerTemplateURL(this)" class="header ">
#         <!----><div ng-if="!template" class="ng-table-header" ng-class="{'sort-indicator': params.settings().sortingIndicator == 'div'}">
#             <span ng-bind="$column.title(this)" ng-class="{'sort-indicator': params.settings().sortingIndicator == 'span'}" class="sort-indicator">Status</span>
#         </div><!---->
#         <!---->
#     </th><!----><!---->
# </tr>
# <tr ng-show="show_filter" class="ng-table-filters ng-hide">
#     <!----><!----><th data-title-text="Financial Year" ng-repeat="$column in $columns" ng-if="$column.show(this)" class="filter " ng-class="params.settings().filterOptions.filterLayout === 'horizontal' ? 'filter-horizontal' : ''">
#         <!---->
#     </th><!----><!----><!----><th data-title-text="Tax Period" ng-repeat="$column in $columns" ng-if="$column.show(this)" class="filter " ng-class="params.settings().filterOptions.filterLayout === 'horizontal' ? 'filter-horizontal' : ''">
#         <!---->
#     </th><!----><!----><!----><th data-title-text="Date of filing" ng-repeat="$column in $columns" ng-if="$column.show(this)" class="filter " ng-class="params.settings().filterOptions.filterLayout === 'horizontal' ? 'filter-horizontal' : ''">
#         <!---->
#     </th><!----><!----><!----><th data-title-text="Status" ng-repeat="$column in $columns" ng-if="$column.show(this)" class="filter " ng-class="params.settings().filterOptions.filterLayout === 'horizontal' ? 'filter-horizontal' : ''">
#         <!---->
#     </th><!----><!---->
# </tr>
# </thead>
#                                 <tbody>
#                                         <!----><tr data-ng-repeat="y in $data[0][rType] | orderBy:['-fy','-orderVal']">
#                                         <td class="text-center" data-title="trans.HEAD_FINAN_YEAR" data-title-text="Financial Year">2017-2018</td>
#                                         <td class="text-center" data-title="trans.LBL_RET_FILING_PERIOD" data-title-text="Tax Period">Annual</td>
#                                         <td class="text-center" data-title="trans.LBL_DT_OF_FILING" data-title-text="Date of filing">07/02/2020</td>
#                                         <td class="text-center" data-title="trans.HEAD_FIL_STAT" data-title-text="Status">Filed</td>
#                                 </tr><!---->
#                             </tbody>
#                         </table><div ng-table-pagination="params" template-url="templates.pagination"><!----><div ng-include="templateUrl"><!----><div class="ng-table-pager" ng-if="params.data.length">
#     <!---->
#     <!---->
# </div><!---->
# </div></div>
# 				        </div>
# 				    </div><!---->
# 				</div>
#             </div><!---->
#             <!---->
#             </div>
# """

from bs4 import BeautifulSoup


def filing_table(soup):
    # soup = BeautifulSoup(html_doc, 'html.parser')
    data = soup.find_all("div", {"class": "table-responsive"})
    yt = {}
    for x in range(1, len(data)):
        body = data[x].find_all("tr")
        head = body[0]
        body_rows = body[2:]
        headings = []
        for item in head.find_all("th"):
            item = item.text.strip("\n")
            headings.append(item)
        all_rows = []
        # print("headings", headings)
        for row_num in range(len(body_rows)):
            row = []
            for row_item in body_rows[row_num].find_all("td"):
                aa = re.sub("(\xa0)|(\n)|,", "", row_item.text)
                row.append(aa.strip())
            all_rows.append(row)

        yg = [dict(zip(headings, x)) for x in all_rows]
        if x == 0:
            yt["GST"] = yg
        if x == 1:
            yt["GSTR3B"] = yg
        elif x == 2:
            yt["GSTR1"] = yg
        else:
            yt["GSTR9"] = yg
    return yt


# filling_table()
