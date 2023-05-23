from xml.dom import minidom


class Report:
    def __init__(self, fail_cases, pass_cases, skip_cases, test_status, total, duration):
        self.fail_cases = fail_cases
        self.pass_cases = pass_cases
        self.test_status = test_status
        self.skip_cases = skip_cases
        self.duration = duration
        self.total = total

        self.doc = minidom.Document()
        root_node = self.doc.createElement('tabs')
        self.doc.appendChild(root_node)
        self.root = root_node

    def gen_report(self):
        self.create_summary_tab()
        if self.test_status != 'PASSED':
            if self.test_status is "SKIPPED":
                self.create_skip_tab()
            else:
                self.create_failure_tab()
        self.gen_total_tab()

        try:
            with open('report.xml', 'w', encoding='UTF-8') as fh:
                self.doc.writexml(fh, indent='', addindent='\t', newl='\n', encoding='UTF-8')
                print("report created!")
        except Exception as err:
            print("report create fail!" + err)

    def create_skip_tab(self):
        return

    def gen_total_tab(self):
        tab_node = self.doc.createElement('tab')
        tab_node.setAttribute('name', 'All Tests')
        self.root.appendChild(tab_node)
        table_node = self.doc.createElement('table')
        tab_node.appendChild(table_node)
        tr_node = self.doc.createElement('tr')
        table_node.appendChild(tr_node)
        td_node = self.doc.createElement('td')
        td_node.setAttribute('value', 'Test Method')
        td_node.setAttribute('fontattribute', 'bold')
        td_node.setAttribute('align', 'center')
        td_node.setAttribute('width', '1000')
        tr_node.appendChild(td_node)

        td_node = self.doc.createElement('td')
        td_node.setAttribute('value', 'Duration')
        td_node.setAttribute('fontattribute', 'bold')
        td_node.setAttribute('align', 'center')
        td_node.setAttribute('width', '300')
        tr_node.appendChild(td_node)

        for pass_case in self.pass_cases:
            case_name = pass_case["caseName"]
            duration_time = self.duration[case_name]

            tr_node = self.doc.createElement('tr')
            table_node.appendChild(tr_node)
            td_node = self.doc.createElement('td')
            td_node.setAttribute('value', case_name)
            td_node.setAttribute('align', 'left')
            td_node.setAttribute('width', '1000')
            td_node.setAttribute('fontcolor', 'green')
            tr_node.appendChild(td_node)

            td_node = self.doc.createElement('td')
            td_node.setAttribute('value', duration_time)
            td_node.setAttribute('align', 'left')
            td_node.setAttribute('width', '300')
            tr_node.appendChild(td_node)

        for fail_case in self.fail_cases:
            case_name = fail_case["caseName"]
            duration_time = self.duration[case_name]

            tr_node = self.doc.createElement('tr')
            table_node.appendChild(tr_node)
            td_node = self.doc.createElement('td')
            td_node.setAttribute('value', case_name)
            td_node.setAttribute('align', 'left')
            td_node.setAttribute('width', '1000')
            td_node.setAttribute('fontcolor', 'red')
            tr_node.appendChild(td_node)

            td_node = self.doc.createElement('td')
            td_node.setAttribute('value', duration_time)
            td_node.setAttribute('align', 'left')
            td_node.setAttribute('width', '300')
            tr_node.appendChild(td_node)

        for skip_case in self.skip_cases:
            case_name = skip_case["caseName"]
            duration_time = self.duration[case_name]

            tr_node = self.doc.createElement('tr')
            table_node.appendChild(tr_node)
            td_node = self.doc.createElement('td')
            td_node.setAttribute('value', case_name)
            td_node.setAttribute('align', 'left')
            td_node.setAttribute('width', '1000')
            td_node.setAttribute('fontcolor', 'yellow')
            tr_node.appendChild(td_node)

            td_node = self.doc.createElement('td')
            td_node.setAttribute('value', duration_time)
            td_node.setAttribute('align', 'left')
            td_node.setAttribute('width', '300')
            tr_node.appendChild(td_node)

    def create_failure_tab(self):
        tab_node = self.doc.createElement('tab')
        tab_node.setAttribute('name', 'Failed Tests')
        self.root.appendChild(tab_node)
        table_node = self.doc.createElement('table')
        tab_node.appendChild(table_node)
        tr_node = self.doc.createElement('tr')
        table_node.appendChild(tr_node)
        td_node = self.doc.createElement('td')
        td_node.setAttribute('value', 'Test Method')
        td_node.setAttribute('fontattribute', 'bold')
        td_node.setAttribute('align', 'center')
        td_node.setAttribute('width', '1000')
        tr_node.appendChild(td_node)

        td_node = self.doc.createElement('td')
        td_node.setAttribute('value', 'Duration')
        td_node.setAttribute('fontattribute', 'bold')
        td_node.setAttribute('align', 'center')
        td_node.setAttribute('width', '300')
        tr_node.appendChild(td_node)

        td_node = self.doc.createElement('td')
        td_node.setAttribute('value', 'Reason')
        td_node.setAttribute('fontattribute', 'bold')
        td_node.setAttribute('align', 'center')
        td_node.setAttribute('width', '2000')
        tr_node.appendChild(td_node)

        for fail_case in self.fail_cases:
            case_name = fail_case["caseName"]
            reason = fail_case["reason"]
            duration_time = self.duration[case_name]

            tr_node = self.doc.createElement('tr')
            table_node.appendChild(tr_node)
            td_node = self.doc.createElement('td')
            td_node.setAttribute('value', case_name)
            td_node.setAttribute('align', 'left')
            td_node.setAttribute('width', '1000')
            tr_node.appendChild(td_node)

            td_node = self.doc.createElement('td')
            td_node.setAttribute('value', duration_time)
            td_node.setAttribute('align', 'left')
            td_node.setAttribute('width', '300')
            tr_node.appendChild(td_node)

            td_node = self.doc.createElement('td')
            td_node.setAttribute('value', reason)
            td_node.setAttribute('align', 'left')
            td_node.setAttribute('width', '2000')
            tr_node.appendChild(td_node)

    def create_summary_tab(self):
        tab_node = self.doc.createElement('tab')
        tab_node.setAttribute('name', 'Overview')
        self.root.appendChild(tab_node)
        table_node = self.doc.createElement('table')
        tab_node.appendChild(table_node)
        tr_node = self.doc.createElement('tr')
        table_node.appendChild(tr_node)
        td_node = self.doc.createElement('td')
        td_node.setAttribute('value', 'Status')
        td_node.setAttribute('fontattribute', 'bold')
        td_node.setAttribute('align', 'center')
        td_node.setAttribute('width', '250')
        tr_node.appendChild(td_node)

        td_node = self.doc.createElement('td')
        td_node.setAttribute('value', 'Total')
        td_node.setAttribute('fontattribute', 'bold')
        td_node.setAttribute('align', 'center')
        td_node.setAttribute('width', '250')
        tr_node.appendChild(td_node)

        td_node = self.doc.createElement('td')
        td_node.setAttribute('value', 'Pass')
        td_node.setAttribute('fontattribute', 'bold')
        td_node.setAttribute('align', 'center')
        td_node.setAttribute('width', '250')
        tr_node.appendChild(td_node)

        td_node = self.doc.createElement('td')
        td_node.setAttribute('value', 'Fail')
        td_node.setAttribute('fontattribute', 'bold')
        td_node.setAttribute('align', 'center')
        td_node.setAttribute('width', '250')
        tr_node.appendChild(td_node)

        td_node = self.doc.createElement('td')
        td_node.setAttribute('value', 'Skip')
        td_node.setAttribute('fontattribute', 'bold')
        td_node.setAttribute('align', 'center')
        td_node.setAttribute('width', '250')
        tr_node.appendChild(td_node)

        tr_node = self.doc.createElement('tr')
        table_node.appendChild(tr_node)
        td_node = self.doc.createElement('td')
        if self.test_status == 'PASSED':
            td_node.setAttribute('fontcolor', 'green')
        else:
            td_node.setAttribute('fontcolor', 'red')
        td_node.setAttribute('value', self.test_status)
        td_node.setAttribute('fontattribute', 'normal')
        td_node.setAttribute('align', 'center')
        td_node.setAttribute('width', '250')
        tr_node.appendChild(td_node)

        td_node = self.doc.createElement('td')
        td_node.setAttribute('value', str(self.total))
        td_node.setAttribute('fontattribute', 'normal')
        td_node.setAttribute('align', 'center')
        td_node.setAttribute('width', '250')
        tr_node.appendChild(td_node)

        td_node = self.doc.createElement('td')
        td_node.setAttribute('value', str(len(self.pass_cases)))
        td_node.setAttribute('fontattribute', 'normal')
        td_node.setAttribute('align', 'center')
        td_node.setAttribute('width', '250')
        tr_node.appendChild(td_node)

        td_node = self.doc.createElement('td')
        td_node.setAttribute('value', str(len(self.fail_cases)))
        td_node.setAttribute('fontattribute', 'normal')
        td_node.setAttribute('align', 'center')
        td_node.setAttribute('width', '250')
        tr_node.appendChild(td_node)

        td_node = self.doc.createElement('td')
        td_node.setAttribute('value', str(len(self.skip_cases)))
        td_node.setAttribute('fontattribute', 'normal')
        td_node.setAttribute('align', 'center')
        td_node.setAttribute('width', '250')
        tr_node.appendChild(td_node)


'''
<section name="" fontcolor="">
    // To display a field
    <field name="" titlecolor="" value="" detailcolor="" href=""> <![CDATA[  ]]> </field>
 
    // To display a table
    <table>
        <tr>
            <td value="" bgcolor="" fontcolor="" title="" fontattribute="" href="" align="" width=""/>
            <td value="" bgcolor="" fontcolor="" title="" fontattribute="" href="" align="" width=""/>
        </tr>
        <tr>
            <td value="" bgcolor="" fontcolor="" title="" fontattribute="" href="" align="" width=""/>
            <td value="" bgcolor="" fontcolor="" title="" fontattribute="" href="" align="" width=""/>
        </tr>
    </table>
 
    // To display tabs
    <tabs>
        <tab name="">
        // Only insert table or field in tab
        </tab>
        <tab name="">
        // Only insert table or field in tab
        </tab>
    </tabs>
 
    // To display an accordion
    <accordion name="">
    // Only insert table or field in tab
    </accordion>
</section>
'''
