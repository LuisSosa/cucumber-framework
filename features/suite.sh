#! /bin/sh
behave -f allure_behave.formatter:AllureFormatter -o features/reports/temp \
features/search.feature \
features/add_product_to_bag.feature \
features/remove_from_bag.feature

sh "features/files.sh"